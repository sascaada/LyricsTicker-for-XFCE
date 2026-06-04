# LyricsTicker for XFCE

Synced lyrics in the XFCE panel.

This project shows the current lyric line of the song playing on your Linux desktop.

It uses:

* playerctl / MPRIS for song info
* LRCLib for synced lyrics
* XFCE Generic Monitor plugin for panel display

## Screenshot

Comin soon.

## Requirements

### Arch Linux

sudo pacman -S playerctl xfce4-genmon-plugin python python-requests noto-fonts-cjk

### Linux Mint / Ubuntu XFCE

sudo apt update

sudo apt install playerctl xfce4-genmon-plugin python3 python3-requests fonts-noto-cjk

## Install

git clone https://github.com/sascaada/LyricsTicker-for-XFCE.git

cd LyricsTicker-for-XFCE

chmod +x install.sh

./install.sh

Then add it to XFCE Panel:

1. Right click panel
2. Panel → Add New Items
3. Add Generic Monitor
4. Set command:

~/.local/bin/xfce-lyrics

5. Set period:

2

Use 1 if your system is fast. Use 2 if the panel feels slow.

## Supported Players

* Spotify desktop app
* VLC
* MPV
* Some browsers

Spotify Web in Firefox may not work because Firefox sometimes only shows:

Firefox is playing media

instead of the real song title and artist.

## Japanese / CJK Lyrics

Arch Linux:

sudo pacman -S noto-fonts-cjk

Linux Mint / Ubuntu:

sudo apt install fonts-noto-cjk

## Uninstall

Remove the installed script:

rm -f ~/.local/bin/xfce-lyrics

Remove cached lyrics:

rm -f /tmp/xfce-lyrics-cache.txt

Remove the XFCE panel item:

1. Right-click the XFCE panel
2. Panel → Panel Preferences
3. Items
4. Select Generic Monitor
5. Click the minus (-) button

Or use:

chmod +x uninstall.sh

./uninstall.sh

## License

MIT License

