from libqtile import layout
from libqtile.config import Match
from settings.theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 3,
    'margin': 12
}

layouts = [layout.MonadTall(**layout_conf),
           layout.RatioTile(**layout_conf),
           layout.Bsp(**layout_conf),
           layout.Max(),
        #    layout.MonadWide(**layout_conf),
        #    layout.Matrix(columns=2, **layout_conf),
        #    layout.Columns(),
        #    layout.Tile(),
        #    layout.TreeTab(),
        #    layout.VerticalTile(),
        #    layout.Zoomy(),
        ]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(title='branchdialog'),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pomotroid"),
        Match(wm_class="cmatrixterm"),
        Match(title="Farge"),
        Match(wm_class="org.gnome.Nautilus"),
        Match(wm_class="feh"),
        Match(wm_class="eog"),
        Match(wm_class="io.elementary.calculator"),
    ],
    border_focus=colors["color4"][0]
)
