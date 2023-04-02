#!/usr/bin/env bash
set -euo pipefail

mute () {
  muted=$(pulsemixer --id source-1 --get-mute)
  if [[ "$muted" == "0" ]]; then
    echo "" > /tmp/micvol-icon
  else
    echo "" > /tmp/micvol-icon
  fi
}

if [ -p /tmp/micvol ] && [ -p /tmp/micvol-icon ]; then
    true
else
    mkfifo /tmp/micvol && echo "$(pulsemixer --id source-1 --get-volume | awk '{print $1}')" > /tmp/micvol 
    mkfifo /tmp/micvol-icon && mute
fi

script_name="micvol.sh"
for pid in $(pgrep -f $script_name); do
    if [ $pid != $$ ]; then
        kill -9 $pid
    fi 
done

start=$SECONDS
value=5

eww_wid="$(xdotool search --name 'Eww - micvol' || true)"

if [ ! -n "$eww_wid" ]; then
    eww open micvol
    eww_wid="$(xdotool search --name 'Eww - micvol' || true)"
fi

case $1 in
    up)
        currentVolume=$(pulsemixer --id source-1 --get-volume | awk '{print $1}')
               if [[ "$currentVolume" -ge "100" ]]; then
                   pulsemixer --max-volume 100 --id source-1
               else
                   pulsemixer --id source-1 --change-volume +"$value"
               fi
    ;;
    down)
        pulsemixer --id source-1 --change-volume -"$value"
    ;;
    mute)
        pulsemixer --toggle-mute --id source-1 
        mute
        #muted=$(pulsemixer --id source-1 --get-mute)
        #    if [[ "$muted" == "0" ]]; then
        #        echo "" > /tmp/micvol-icon
        #    else 
        #        echo "" > /tmp/micvol-icon
        #    fi
    ;;
esac

echo $(pulsemixer --id source-1 --get-volume | awk '{print $1}') > /tmp/micvol 

while [ -n "$eww_wid" ]; do
    duration=$(( SECONDS - start ))
    if [[ $duration -gt 1 ]]; then
        eww close micvol
        eww_wid="$(xdotool search --name 'Eww - micvol' || true)"       
    fi
    sleep 0.2
done

