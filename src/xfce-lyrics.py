#!/usr/bin/env python3
import html
import re
import subprocess
import time
import requests

MAX_LEN = 70
CACHE = "/tmp/xfce-lyrics-cache.txt"

def run(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def clean_title(title):
    title = re.sub(r"\(.*?\)|\[.*?\]", "", title)
    title = title.replace(" - Spotify", "")
    return title.strip()

def get_metadata():
    title = clean_title(run("playerctl metadata xesam:title"))
    artist = run("playerctl metadata xesam:artist")
    pos = float(run("playerctl position"))
    return title, artist, pos

def parse_lrc(lrc):
    lines = []
    for row in lrc.splitlines():
        m = re.match(r"\[(\d+):(\d+\.\d+)\](.*)", row)
        if m:
            sec = int(m.group(1)) * 60 + float(m.group(2))
            text = m.group(3).strip()
            if text:
                lines.append((sec, text))
    return lines

def fetch_lyrics(title, artist):
    r = requests.get(
        "https://lrclib.net/api/get",
        params={"track_name": title, "artist_name": artist},
        timeout=5
    )
    data = r.json()
    return data.get("syncedLyrics") or ""

def current_line(lines, pos):
    now = ""
    for sec, text in lines:
        if sec <= pos:
            now = text
        else:
            break
    return now

try:
    title, artist, pos = get_metadata()
    key = f"{artist} - {title}"

    try:
        old_key, old_lrc = open(CACHE).read().split("\n", 1)
    except:
        old_key, old_lrc = "", ""

    if old_key != key:
        lrc = fetch_lyrics(title, artist)
        open(CACHE, "w").write(key + "\n" + lrc)
    else:
        lrc = old_lrc

    lines = parse_lrc(lrc)

    if lines:
        text = current_line(lines, pos)
    else:
        text = key

    if not text:
        text = key

    text = "♪ " + text[:MAX_LEN]
    print(text)

except Exception:
    print("♪")
