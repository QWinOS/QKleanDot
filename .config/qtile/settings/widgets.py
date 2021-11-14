import os
from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

# Enter Your Location Here
location = 'Asansol'

# Enter User password in line 99

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(fg="light", bg="dark", t=" "):
    return widget.TextBox(**base(fg,bg), text=t, fontsize = 5, padding=5)


def icon(fg='light', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )

def workspaces():
    return [
        # separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=22,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='text',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True,
            hide_unused=True
        ),
        # widget.WindowName(**base(fg='focus'), fontsize=13, padding=5),
    ]


primary_widgets = [
    # Current Layout
    widget.CurrentLayoutIcon(**base(bg='color4'), scale=0.7),
    widget.CurrentLayout(**base(bg='color4'), padding=5),

    *workspaces(),
    
    widget.Spacer(**base()),

    # Weather
    widget.WidgetBox(**base(fg='color2'), 
                    widgets=[widget.Wttr(**base(fg='color2'), location={location:''}, format="Feels like %f |  %h | 煮  %w | %m%M |   %p |  %P | " , update_interval=60)],
                    text_closed="{}".format(location), text_open="{}  ".format(location)),
    widget.Wttr(**base(fg='color2'), location={location:''}, format="%c%t" , update_interval=60),

    separator(),

    # CPU/RAM
    widget.WidgetBox(**base(fg='color3'), 
                    widgets=[widget.CPU(**base(fg='color3'),format="CPU {freq_current}GHz {load_percent}% "),
                    widget.CPUGraph(**base(fg='color3')),
                    widget.TextBox(**base(fg='color3'),text=" RAM ")],
                    text_closed=' ',text_open=' ',fontsize=20),
    widget.Memory(**base(fg='color3'), measure_mem="G",format="{MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}"),

    separator(),

    # Check Updates
    # icon(fg="color5", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(**base(fg='color5'),
    colour_have_updates=colors['color5'],colour_no_updates=colors['color5'],no_update_string='No updates', execute="echo -e 'ENTER_USER_PASS_HERE' | sudo -S sudo powerpill --noconfirm -Su && paru --noconfirm -Su && notify-send 'System Updated'"),

    separator(),
                        
    # Battery
    widget.Battery(**base(fg='color6'),charge_char=' ',discharge_char=' ',full_char=' ',empty_char=' ', 
                    format="{char} {percent:2.0%}" , update_interval=30),

    # Backlight
    # widget.Backlight(**base(bg='color5'),backlight_name='amdgpu_bl0',format=' {percent:2.0%} ﯦ '),

    # System Tray
    widget.Systray(**base(fg='color7'), padding=5),

    # Extras
    widget.WidgetBox(**base(fg="color1"), widgets=[icon(fg="color1", text=' '),  # Icon: nf-fa-feed
                              widget.Net(**base(fg='color1'), interface='wlo1', format='{down}↓{up}↑')],
                              text_closed=' ﰪ ',text_open='  ',fontsize=18),
    
    separator(),

    # Time Date
    widget.WidgetBox(**base(fg="color2"), widgets=[widget.Clock(**base(fg='color2'), 
                                                   format='%A ')], text_closed='   ',text_open=' '),
    widget.Clock(**base(fg='color2'), format='%d/%m/%y %I:%M %p ',
    mouse_callbacks={
        # "Button1": lambda: os.system('dunstify "$(cal)"')
        }),
]


# For Secondary Display
# secondary_widgets = [
# *workspaces(),
# separator(),
# powerline('color1', 'dark'),
# widget.Memory(**base(bg='color5'), measure_mem='G'),
# widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
# widget.CurrentLayout(**base(bg='color1'), padding=5),
# powerline('color2', 'color1'),
# widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
# widget.Volume(**base(bg='color3')),
# powerline('dark', 'color2'),
# ]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
