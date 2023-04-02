#!/usr/bin/bash

echo "123" | sudo mv wakelock@.service /usr/lib/systemd/system/
sudo systemctl enable wakelock@angshuman

sudo pacman -S auto-cpufreq eww i3lock-color xautolock flashfocus
