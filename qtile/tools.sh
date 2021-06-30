SELECT=$(echo " Sublime Text
 Vim
 Pcmanfm
 Bauh
 Vivaldi
 Freetube
 Netflix
 Altus
 Bpytop" | rofi -dmenu -lines 9 -width 15 -p "Herramientas")

[[ -z $SELECT ]] && exit

if [[ $SELECT == " Sublime Text" ]];then
    subl
elif [[ $SELECT == " Vim" ]];then
    alacritty -e nvim 
elif [[ $SELECT == " Pcmanfm" ]];then
    pcmanfm &
elif [[ $SELECT == " Vivaldi" ]];then
    vivaldi-snapshot &
elif [[ $SELECT == " Netflix" ]];then
    qtws /usr/share/qtws-apps/netflix/netflix.qtws &
elif [[ $SELECT == " Altus" ]];then
    ~/.local/share/bauh/appimage/installed/altus/"Altus-4.2.0-x86_64.AppImage" &
elif [[ $SELECT == " Bauh" ]];then
    bauh &
elif [[ $SELECT == " Freetube" ]];then
    ~/.local/share/bauh/appimage/installed/freetube/"freetube_0.13.2_amd64.AppImage" &
elif [[ $SELECT == " Bpytop" ]];then
    alacritty -e bpytop
else
    echo $SELECT
fi
