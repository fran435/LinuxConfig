#!/usr/bin/env python3
import os
from rofi import rofi

select = rofi("Init\nPlay\nStop\nNext\nPrev\nSearch track", "CMUS")
    
if select == "Init\n":
    os.system("alacritty -e cmus")
    
elif select == "Play\n":
    os.system("cmus-remote -p")
    
elif select == "Stop\n":
    os.system("cmus-remote -u")
    
elif select == "Next\n":
    os.system("cmus-remote -n")
    
elif select == "Prev\n":
    os.system("cmus-remote -r")
    
elif select == "Search track":
    os.system("cmus-remote -u") 
    
else:
    print("Select es igual a: '{0}'".format(select))
