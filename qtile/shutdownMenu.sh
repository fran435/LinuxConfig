SELECT=$(echo " Shutdown
 Reboot
 Logout" | rofi -dmenu -lines 3 -width 10 -p "Shutdown Menu")

[[ -z "$SELECT" ]] && exit

CONFIRM=$(rofi -dmenu -lines 0 -width 13 -p "Are you sure? (y/N)")

if [[ "$CONFIRM" == "y" ]]; then
    if [[ "$SELECT" == " Shutdown" ]]; then
        systemctl poweroff
    elif [[ "$SELECT" == " Reboot" ]]; then
        systemctl reboot
    elif [[ "$SELECT" == " Logout" ]]; then
        systemctl restart display-manager
    fi
fi
