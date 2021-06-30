from libqtile.lazy import lazy
from libqtile import bar,  widget
from libqtile.config import Screen

widget_defaults = dict(
    font='Sans',
    fontsize=16,
    padding=5
)

extension_defaults = widget_defaults.copy()

clk_bg = "#CC3535"
vol_bg = "#00FA9A"
RAM_bg = "#FF4500"
CPU_bg = "#FF8C00"
NET_bg = "#FFD700"
gs_bg = "#1E90FF"
gs_act = "#ADFF2F"
g_sel = "#FFD700"
g_urg = "#FF4500"
bar_bg = "#383A36"

screens = [
    Screen(
        bottom=bar.Bar(
            [

                widget.GroupBox(
                    active = gs_act,
                    background = gs_bg,
                    highlight_method = "text",
                    this_current_screen_border = g_sel,
                    urgent_alert_method = "text",
                    urgent_text = g_urg,
                    fontsize = 20,
                    font = "DejaVuSansMono NF",
                    borderwidth = 0,
                    padding_x = 5
                ),

                widget.TextBox(
                    foreground = gs_bg,
                    background = vol_bg,
                    text = "",
                    fontsize = 30,
                    padding = 0
                ),

                widget.Volume(
                    fontsize = 15,
                    font = "DejaVuSansMono NF",
                    background = vol_bg,
                    foreground = bar_bg
                    ),

                widget.TextBox(
                    foreground = vol_bg,
                    text = "",
                    fontsize = 30,
                    padding = 0
                ),

                widget.WindowName(
                    fontsize = 15,
                    font = "DejaVuSansMono NF"
                ),

                widget.Notify(),

                widget.TextBox(
                    background = bar_bg,
                    foreground = NET_bg,
                    text = "",
                    fontsize = 30,
                    padding = 0
                ),

                widget.NetGraph(
                    background = NET_bg
                ),

                widget.TextBox(
                    background = NET_bg,
                    foreground = CPU_bg,
                    text = "",
                    fontsize = 30,
                    padding = 0
                ),

                widget.CPUGraph(
                    background = CPU_bg
                ),
                
                widget.TextBox(
                    background = CPU_bg,
                    foreground = RAM_bg,
                    text = "",
                    fontsize = 30,
                    padding = 0
                ),

                widget.MemoryGraph(
                    background = RAM_bg,
                ), 

                widget.TextBox(
                    background = RAM_bg,
                    foreground = clk_bg,
                    text = "",
                    fontsize = 30,
                    padding = 0
                ),

                widget.Clock(
                    background = clk_bg,
                    fontsize = 15,
                    format='%I:%M %p'
                )
            ],
            25,
            background = bar_bg
        ),
    ),
]
