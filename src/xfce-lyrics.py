#!/usr/bin/env python3
import os, re, subprocess, json, urllib.parse

CACHE = "/tmp/xfce-lyrics-cache.txt"
STATE = "/tmp/xfce-lyrics-state.txt"
MAX_LEN = 70

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def clean_title(t):
    return re.sub(r"\(.*?\)|\[.*?\]", "", t).replace(" - Spotify", "").strip()

def get_meta():
    title = clean_title(run("playerctl metadata xesam:title"))
    artist = run("playerctl metadata xesam:artist")
    pos = float(run("playerctl position"))
    return title, artist, pos

def parse_lrc(lrc):
    out = []
    for row in lrc.splitlines():
        m = re.match(r"\[(\d+):(\d+(?:\.\d+)?)\](.*)", row)
        if m:
            sec = int(m.group(1))*60 + float(m.group(2))
            text = m.group(3).strip()
            if text:
                out.append((sec, text))
    return out

def fetch(title, artist):
    query = urllib.parse.quote(f"{artist} {title}".strip())
    url = f"https://lrclib.net/api/search?q={query}"

    try:
        raw = run(f'curl -L --max-time 12 -s "{url}"')
        results = json.loads(raw)

        for item in results:
            synced = item.get("syncedLyrics")
            if synced:
                return synced
    except:
        pass

    return ""

try:
    title, artist, pos = get_meta()
    key = f"{artist} - {title}"

    old_key = ""
    old_lrc = ""
    if os.path.exists(STATE):
        old_key = open(STATE).read().strip()
    if os.path.exists(CACHE):
        old_lrc = open(CACHE).read()

    if key != old_key:
        lrc = fetch(title, artist)
        open(STATE, "w").write(key)
        open(CACHE, "w").write(lrc)
    else:
        lrc = old_lrc

    lines = parse_lrc(lrc)
    text = ""

    for sec, line in lines:
        if sec <= pos:
            text = line
        else:
            break

    if not text:
        text = key

    print("♪ " + text[:MAX_LEN])

except:
    print("♪")
