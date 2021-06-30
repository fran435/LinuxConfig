from libqtile import hook
import os
import random

from screens import *
from keys import *
from groups import *
from layouts import *

@hook.subscribe.startup_complete
def autostart():

    cmd=[
        "feh --bg-fill /home/fran/Imágenes/wallpapers/wall{0}*".format(str(random.randint(0,7))) ,
        "picom -b",
        "setxkbmap es",
        "vivaldi-snapshot &",
        "alacritty &"
    ]

    for command in cmd:
        os.system(command)

dgroups_key_binder = None
main = None
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "Qtile"
