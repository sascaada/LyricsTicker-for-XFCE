# LyricsTicker for XFCE

Synced lyrics in the XFCE panel.

This project shows the current lyric line of the song playing on your Linux desktop.

It uses:

* playerctl / MPRIS for song info
* LRCLib for synced lyrics
* XFCE Generic Monitor plugin for panel display

## Screenshot

<img width="1825" height="1042" alt="image" src="https://github.com/user-attachments/assets/b02f1b99-5800-462f-8053-74d90c3d9662" />
<img width="2070" height="1020" alt="image" src="https://github.com/user-attachments/assets/4dbbd236-7604-4392-906d-e9c0b52ed7f8" />
<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/e72ece6c-2a6c-4647-9843-2ef282dc2e45" />
<img width="1599" height="899" alt="image" src="https://github.com/user-attachments/assets/3798f282-0378-494c-9bd8-6440a25cdc35" />



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

