#!/usr/bin/env bash

theme="circle"
dir="$HOME/.config/rofi/powermenu"

# random colors
styles=($(ls -p --hide="colors.rasi" $dir/styles))
color="${styles[$(( $RANDOM % 8 ))]}"

# comment this line to disable random colors
sed -i -e "s/@import .*/@import \"$color\"/g" $dir/styles/colors.rasi

# comment these lines to disable random style
# themes=($(ls -p --hide="powermenu.sh" --hide="styles" --hide="confirm.rasi" --hide="message.rasi" $dir))
# theme="${themes[$(( $RANDOM % 24 ))]}"

uptime=$(uptime -p | sed -e 's/up //g')

rofi_command="rofi -theme $dir/$theme"

# Options
yess="Yes"
noo="No"
shutdown=" ⏻ "
reboot=" 勒 "
suspend=" 鈴 "
logout="  "

# Confirmation
confirm_exit() {
	choice="$yess\n$noo"
	# rofi -dmenu -i -no-fixed-num-lines 
	choosed="$(echo -e "$choice" | rofi -theme $dir/confirm.rasi -dmenu -selected-row 1 -p "Are You Sure? : " )"
	case $choosed in
		$yess)
			echo 1;;
		$noo)
			echo 0;;
	esac
}

# Message
msg() {
	rofi -theme "$dir/message.rasi" -e "Available Options  -  yes / y / no / n"
}

# Variable passed to rofi
options="$shutdown\n$reboot\n$suspend\n$logout"

chosen="$(echo -e "$options" | $rofi_command -p "Uptime: $uptime" -dmenu -selected-row 0)"
case $chosen in
    $shutdown)
		ans=$(confirm_exit &)
		if [[ $ans == 1 ]]; then
			systemctl poweroff
		else
			exit 0
        fi
        ;;
    $reboot)
		ans=$(confirm_exit &)
		if [[ $ans == 1 ]]; then
			systemctl reboot
		else
			exit 0
        fi
        ;;
    $suspend)
		ans=$(confirm_exit &)
		if [[ $ans == 1 ]]; then
			playerctl pause
			# pamixer -m
			systemctl suspend
		else
			exit 0
        fi
        ;;
    $logout)
		ans=$(confirm_exit &)
		if [[ $ans == 1 ]]; then
			killall xinit
		else
			exit 0
        fi
        ;;
esac
