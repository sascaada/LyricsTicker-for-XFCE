#!/bin/bash

mkdir -p ~/.local/bin
cp src/xfce-lyrics.py ~/.local/bin/xfce-lyrics
chmod +x ~/.local/bin/xfce-lyrics

echo "Installed LyricsTicker for XFCE!"
echo ""
echo "Now add XFCE Generic Monitor to panel:"
echo "Command: $HOME/.local/bin/xfce-lyrics"
echo "Period: 2"
