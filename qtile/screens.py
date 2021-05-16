#from widgets import HolaMundo
from libqtile import bar,  widget
from libqtile.config import Screen

widget_defaults = dict(
    font='Sans',
    fontsize=16,
    padding=5
)

extension_defaults = widget_defaults.copy()

gs_bg = "#3F58CA"
gs_act = "#43A047"
g_sel = "#FFC107"
g_urg = "#EF5350"
bar_bg = "#383A36"

screens = [
    Screen(
        top=bar.Bar(
            [ 

                widget.WindowName(foreground = bar_bg),

                widget.TextBox(
                    foreground = gs_bg,
                    text = "",
                    fontsize = 25,
                    padding = 0
                ),

                widget.GroupBox(
                    active = gs_act,
                    background = gs_bg,
                    highlight_method = "text",
                    this_current_screen_border = g_sel,
                    urgent_alert_method = "text",
                    urgent_text = g_urg,
                    fontsize = 25,
                    font = "DejaVuSansMono NF",
                    borderwidth = 0,
                    padding_x = 5
                ),

                widget.TextBox(
                    foreground = gs_bg,
                    text = "",
                    fontsize = 25,
                    padding = 0
                ),

                widget.WindowName(foreground = bar_bg),

                widget.Clock(format='%I:%M %p')
            ],
            32,
            margin = 10,
            background = bar_bg
        ),
    ),
]
