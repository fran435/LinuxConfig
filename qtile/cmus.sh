SELECT=$(echo "襤 On/Off
懶 Play/Stop
怜 Next
玲 Prev
 Search track
墳 Volume" | rofi -dmenu -lines 6 -width 15 -p "Cmus")

[[ -z $SELECT ]] && exit

if [[ $SELECT == "襤 On/Off" ]]; then
    cmus 2> aux.txt
    output=$(cat aux.txt)
    rm aux.txt
    if [[ $output == "cmus: cmus is already listening on socket"* ]]; then
        cmus-remote -C quit
    fi
fi
