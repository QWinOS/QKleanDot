#!/bin/sh

# Start Geo location service
/usr/lib/geoclue-2.0/demos/agent &

# start volume icon
volumeicon &

# start network icon
nm-applet &

# Set Wallpaper (static)
feh --randomize --bg-fill -D 2 ~/Wallpapers/* &

# Set Wallpaper (dynamic)
# dwall -p -s earth &

# start notification manager
dunst &

# start compositor
picom --experimental-backends --backend glx --xrender-sync-fence &

# start auto noise cancellation
noisetorch -i &

# start night light
redshift &

# start auto mouse hider
unclutter --start-hidden &

# refresh pacman database
# echo -e 'YOUR_PASSWORD_HERE' | sudo -S pacman --noconfirm -Sy &

# Battery icon
# cbatticon -n -c "notify-send -u critical \"Low Battery\"" &
