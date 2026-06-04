# LyricsTicker for XFCE

Synced lyrics in the XFCE panel.

This project shows the current lyric line of the song playing on your Linux desktop.

It uses:
- playerctl / MPRIS for song info
- LRCLib for synced lyrics
- XFCE Generic Monitor plugin for panel display

## Screenshot

Coming soon.

## Requirements

On Arch Linux:

```bash
sudo pacman -S playerctl xfce4-genmon-plugin python python-requests noto-fonts-cjk

## Install

```bash
git clone https://github.com/sascaada/LyricsTicker-for-XFCE.git
cd LyricsTicker-for-XFCE
chmod +x install.sh
./install.sh

Then add it to XFCE Panel:

Right click panel
Panel → Add New Items
Add Generic Monitor
Command:

```bash
~/.local/bin/xfce-lyrics

Period: 1/1.75/2

##Uninstall
Remove the installed script:
rm -f ~/.local/bin/xfce-lyrics
Remove cached lyrics:
rm -f /tmp/xfce-lyrics-cache.txt
Remove the XFCE panel item:
Right-click the XFCE panel
Panel → Panel Preferences
Items
Select “Generic Monitor”
Click the minus (-) button
Or if you created uninstall.sh:
chmod +x uninstall.sh
./uninstall.sh
