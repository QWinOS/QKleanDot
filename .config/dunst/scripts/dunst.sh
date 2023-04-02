#!/usr/bin/env bash

status() {
  state=$(dunstctl is-paused)
  if [ "$state" == "false" ]; then
    echo ""
  else
    echo "<span foreground='#3b4252'></span>"
  fi
}


case "$1" in
  --toggle|-t)
    if [ "$(dunstctl is-paused)" = "false" ];then
        dunstify -u normal -a dunst -t 3000 -r 669 "Dunst disabled"
        sleep 3
    else
         dunstify -u normal -a dunst -t 3000 -r 669 "Dunst enabled"
    fi
    dunstctl set-paused toggle
    ;;
  --notif-center|-nc)
    ./.config/rofi/notification/notification_center.sh
    ;;
  *)
    status
    ;;
esac
