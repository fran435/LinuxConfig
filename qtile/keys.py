from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import groups

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Foco de la pantalla
    Key([mod], "h",     lazy.layout.left()),
    Key([mod], "l",     lazy.layout.right()),
    Key([mod], "j",     lazy.layout.down()),
    Key([mod], "k",     lazy.layout.up()),
    Key([mod], "space", lazy.layout.next()),

    # Mover ventanas
    Key([mod, "mod1"], "h", lazy.layout.shuffle_left()),
    Key([mod, "mod1"], "l", lazy.layout.shuffle_right()),
    Key([mod, "mod1"], "j", lazy.layout.shuffle_down()),
    Key([mod, "mod1"], "k", lazy.layout.shuffle_up()),

    # Agrandar ventanas
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    # Cerrar ventanas
    Key([mod], "w", lazy.window.kill()),

    # Reiniciar tamaño de ventanas
    Key([mod], "n", lazy.layout.normalize()),

    # Reinicia Qtile
    Key([mod, "control"], "r", lazy.restart()),

    # Cierra qtile y manda al menú de inicio
    Key([mod, "control"], "q", lazy.shutdown()),

    # Cambia entre entre un layout y otro
    Key([mod], "Tab", lazy.next_layout()),

    # Lanza una terminal
    Key([mod], "Return", lazy.spawn(terminal)),

    # Lanza rofi
    Key([mod],"e", lazy.spawn("rofi -show run"))
]

for i in groups.groups:
    keys.extend([

        # Cambia al grupo i
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # Mueve la ventana actual al grupo i
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True))
    ])

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
