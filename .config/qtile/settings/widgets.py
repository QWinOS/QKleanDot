import os
from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

# Enter Your Location Here
location = 'Burnpur'

# Enter User password in line 86 to update on click via top bar

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator(fg="light", bg="dark", t=" "):
    return widget.TextBox(**base(fg,bg), text=t, fontsize = 5, padding=5)


def icon(fg='light', bg='dark', fontsize=16, text="?", padding=3):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=padding
    )

def tasklistStringHide(text):
    text = text.replace(text,"")
    return text

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
            **base(bg='color4'),
            fontsize=18,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=False,
            hide_unused=True
        ),
    ]


primary_widgets = [
    # Current Layout
    widget.CurrentLayoutIcon(**base(bg='color4'), scale=0.7),
    widget.CurrentLayout(**base(bg='color4',fg='dark'), padding=5),

    *workspaces(),

    widget.TaskList(**base(),highlight_method='block',margin_y=0,parse_text=tasklistStringHide,icon_size=17,txt_floating='',fontsize=20),

    widget.Spacer(**base()),

    # Check Updates
    # icon(fg="color5", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(**base(fg='color4'),
    colour_have_updates=colors['color4'],colour_no_updates=colors['color4'],no_update_string='No updates', execute="echo -e 'ENTER_YOUR_PASSWORD' | sudo -S sudo powerpill --noconfirm -Su && paru --noconfirm -Su && notify-send 'System Updated'"),

    separator(),

    # CPU/RAM
    widget.WidgetBox(**base(fg='color3'), 
                    widgets=[widget.CPU(**base(fg='color3'),format="CPU {freq_current}GHz {load_percent}% "),
                    widget.CPUGraph(**base(fg='color3')),
                    widget.TextBox(**base(fg='color3'),text=" RAM ")],
                    text_closed=' ',text_open=' ',fontsize=20),
    widget.Memory(**base(fg='color3'), measure_mem="G",format="{MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}"),

    separator(),
    
    # Network Speed
    widget.WidgetBox(**base(fg='color5'), widgets=[widget.Net(**base(fg='color5'), format='{up}↑')],text_closed=' ',text_open='  ',fontsize=15),
    widget.Net(**base(fg='color5'), format='{down}↓'),

    separator(),

    # Weather
    widget.WidgetBox(**base(fg='color2'), 
                    widgets=[widget.Wttr(**base(fg='color2'), location={location:''}, format="Feels like %f |  %h | 煮  %w | %m%M |   %p |  %P | " , update_interval=60)],
                    text_closed="{}:".format(location), text_open="{}  ".format(location)),
    widget.Wttr(**base(fg='color2'), location={location:''},format="%c%t" , update_interval=60),

    separator(),

    # System Tray
    widget.Systray(**base(), padding=5),
    
    separator(),

    # Time Date
    widget.WidgetBox(**base(fg='color6'), widgets=[widget.Clock(**base(fg='color6'), 
                                                   format='%A ')], text_closed='   ',text_open=' '),
    widget.Clock(**base(fg='color6'), format='%d/%m/%y %I:%M %p ',
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
