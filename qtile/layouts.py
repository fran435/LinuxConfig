from libqtile import layout

MARGIN = 10

BORDER_NORMAL = "#32302f"
BORDER_FOCUS ="#cc241d"
BORDER_WIDTH = 3

floating_layout = layout.Floating(
    border_normal=BORDER_NORMAL,
    border_focus=BORDER_FOCUS,
    border_width=BORDER_WIDTH,
    float_rules=[
        *layout.Floating.default_float_rules,
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'gcr-prompter'},
        {'wmclass': 'confirmreset'},
        {'wmclass': 'makebranch'},
        {'wmclass': 'maketag'},
        {'wmclass': 'peek'},
        {'wname': 'branchdialog'},
        {'wname': 'pinentry'},
        {'wmclass': 'ssh-askpass'},
    ]
)

layouts = [

    layout.Columns(
        border_normal=BORDER_NORMAL,
        border_focus=BORDER_FOCUS,
        border_width=BORDER_WIDTH,
        num_columns = 3,
        margin=MARGIN
    ),

    layout.Max(
        border_normal=BORDER_NORMAL,
        border_focus=BORDER_FOCUS,
        border_width=BORDER_WIDTH,
        margin=MARGIN
    ),

    layout.Matrix(
        border_normal=BORDER_NORMAL,
        border_focus=BORDER_FOCUS,
        border_width=BORDER_WIDTH,
        margin=MARGIN
    ),

    layout.Tile(
        border_normal=BORDER_NORMAL,
        border_focus=BORDER_FOCUS,
        border_width=BORDER_WIDTH,
        margin=MARGIN
    ),

    layout.TreeTab(
        border_normal=BORDER_NORMAL,
        border_focus=BORDER_FOCUS,
        border_width=BORDER_WIDTH,
        margin=MARGIN
    )
]

