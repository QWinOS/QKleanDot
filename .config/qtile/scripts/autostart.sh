#!/bin/sh

# Start Geo location service
/usr/lib/geoclue-2.0/demos/agent &

# start volume icon
volumeicon &

# start network icon
nm-applet &

# bluetooth icon
blueman-applet &

# Activate auto sleep and autolock after inactivity
# xautolock -time 5 -locker "~/.local/scripts/screen/lockinLogout/screenlock --xautolock" -killtime 10 -killer "systemctl suspend" -detectsleep &
xidlehook --not-when-fullscreen --timer 300 'brightnessctl -qs set 0' 'brightnessctl -r' --timer 30 '~/.local/scripts/screen/lockinLogout/screenlock --xidlehook' '' --timer 600 'systemctl suspend' '' &

# Set Wallpaper (static)
# To set random picture from Wallpapers folder
# feh --randomize --bg-fill ~/Wallpapers/* &
# feh --bg-fill ~/.images/emoji.jpg &

# Set Wallpaper (dynamic)
# dwall -p -s earth &

# start notification manager
dunst &

# start compositor
picom --backend glx --xrender-sync-fence &

# start auto noise cancellation
noisetorch -i &

# start night light
redshift &

# start auto mouse hider
unclutter --start-hidden &

# refresh pacman database
echo -e "$1" | sudo -S pacman --noconfirm -Sy &

# eww daemon start
eww daemon &

# update pywal pallete
wal -i ~/.images/emoji.jpg

# initialize volume icon on volume slider 
mkfifo /tmp/vol && echo "$(pulsemixer --get-volume | awk '{print $1}')" > /tmp/vol &
mkfifo /tmp/vol-icon && ~/.config/eww/scripts/vol_icon.sh &

# initialize mic volume icon on volume slider 
mkfifo /tmp/micvol && echo "$(pulsemixer --id source-1 --get-volume | awk '{print $1}')" > /tmp/micvol &
mkfifo /tmp/micvol-icon && ~/.config/eww/scripts/micvol_icon.sh &

# Start flashfocus (to highlight foucused window)
flashfocus &

# Battery icon
cbatticon -n -c "notify-send -a Battery -i /usr/share/icons/Dracula/symbolic/devices/battery-symbolic.svg -u critical \"Low Battery\"" &

# auto mount usb to linux
udiskie --automount --notify --tray &
