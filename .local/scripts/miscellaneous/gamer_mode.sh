#!/bin/sh

# Epic gamer mode activate!
killall unclutter
dunstctl set-paused true
systemctl --user stop picom

# Gamer time 😎
"$@"

# Le epic gamer mode deactivate!
unclutter --start-hiden &
dunstctl set-paused false
systemctl --user start picom
