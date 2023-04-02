#!/usr/bin/env bash
set -euo pipefail

if [ -p /tmp/bright ]; then
    true
else
    mkfifo /tmp/bright && echo "scale=1; $(brightnessctl get) / 255 * 100" | bc > /tmp/bright 
fi

script_name="bright.sh"
for pid in $(pgrep -f $script_name); do
    if [ $pid != $$ ]; then
        kill -9 $pid
    fi 
done

start=$SECONDS
value=10

eww_wid="$(xdotool search --name 'Eww - bright' || true)"

if [ ! -n "$eww_wid" ]; then
    eww open bright
    eww_wid="$(xdotool search --name 'Eww - bright' || true)"
fi

case $1 in
    up)
        brightnessctl set +"$value"%
    ;;
    down)
        brightnessctl set "$value"%-
    ;;
esac

echo "scale=1; $(brightnessctl get) / 255 * 100" | bc > /tmp/bright 

while [ -n "$eww_wid" ]; do
    duration=$(( SECONDS - start ))
    if [[ $duration -gt 1 ]]; then
        eww close bright
        eww_wid="$(xdotool search --name 'Eww - bright' || true)"       
    fi
    sleep 0.2
done

