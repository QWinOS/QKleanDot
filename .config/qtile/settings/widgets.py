import os
from libqtile import widget, qtile
from settings.theme import colors
import subprocess
from details import *

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
            **base(bg='darker'),
            fontsize=18,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=True,
            highlight_method='text',
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

# Define functions for bar
def dunst():
    return subprocess.check_output(["./.config/dunst/scripts/dunst.sh"]).decode("utf-8").strip()

def toggle_dunst():
    qtile.cmd_spawn("./.config/dunst/scripts/dunst.sh --toggle")

def toggle_notif_center():
    qtile.cmd_spawn("./.config/dunst/scripts/dunst.sh --notif-center")

# Bar Config
primary_widgets = [
    # Current Layout and Workspace
    widget.TextBox(**base(fg='darker'),text=" ",fontsize=20,padding=0),
    widget.CurrentLayoutIcon(**base(bg='darker'), scale=0.7),
    widget.WidgetBox(**base(bg='darker',fg='light'),widgets=[widget.CurrentLayout(**base(bg='darker',fg='light'),padding=5)],
                     text_closed='',text_open='',fontsize=20),
    *workspaces(),
    widget.TextBox(**base(fg='darker'),text=" ",fontsize=20.5,padding=-1),

    # Open Apps List
    widget.TaskList(**base(),highlight_method='block',margin_y=0,theme_mode='fallback',parse_text=tasklistStringHide,theme_path="/usr/share/icons/Dracula/scalable/apps/",icon_size=24,txt_floating='',txt_minimized='',fontsize=24),

    widget.Spacer(**base()),

    # Time Date
    widget.WidgetBox(**base(fg='color6'), widgets=[widget.Clock(**base(fg='color6'),fontsize=18,format=' %b %d, %Y ')],fontsize=20, text_closed='',text_open=''),
    widget.Clock(**base(fg='color6'),fontsize=18,format=' %a ',
    mouse_callbacks={
        # "Button1": lambda: os.system('dunstify "$(cal)"')
        }),
    widget.Clock(**base(fg='color6'),format=" %I:%M %p ",fontsize=18),

    # Media info
    widget.WidgetBox(**base(fg='color6'),widgets=[widget.Mpris2(**base(fg='color6'),poll_interval=0.1,paused_text=' {track}',width=500,scroll=True)],
                     text_closed='',text_open=' ',fontsize=20),

    widget.Spacer(**base()),

    # Network Speed
    widget.TextBox(**base(fg='darker'),text="",fontsize=20,padding=0),
    widget.WidgetBox(**base(bg='darker',fg='color1'), widgets=[widget.NetGraph(**base(bg='darker',fg='color1'),graph_color=colors['color1'],border_width=0),
                                                               widget.Net(**base(bg='darker',fg='color1'),fontsize=18,format='{up}↑')],
                     text_closed='',text_open='',fontsize=20),
    widget.Net(**base(bg='darker',fg='color1'),fontsize=18,format='↓{down}'),
    widget.TextBox(**base(fg='darker'),text=" ",fontsize=20.5,padding=-1),

    # CPU/RAM
    widget.TextBox(**base(fg='darker'),text="",fontsize=20,padding=0),
    widget.WidgetBox(**base(bg='darker',fg='color3'), 
                    widgets=[widget.CPU(**base(bg='darker',fg='color3'),fontsize=18,format=" {freq_current}GHz {load_percent}% "),
                             widget.ThermalZone(**base(bg='darker'),fgcolor_normal=colors['color3']),
                             widget.CPUGraph(**base(bg='darker',fg='color3'),fontsize=18,graph_color=colors['color3'],border_width=0),
                             #widget.NvidiaSensors(**base(bg='darker',fg='color3')),
                             ],
                    text_closed='',text_open='',fontsize=25),
    widget.Memory(**base(bg='darker',fg='color3'),fontsize=18,measure_mem="G",format=" {MemUsed:.1f}{mm}/{MemTotal:.0f}{mm}"),
    widget.TextBox(**base(fg='darker'),text=" ",fontsize=20.5,padding=-1),

    # Miscellaneous
    widget.TextBox(**base(fg='darker'),text="",fontsize=20,padding=0),
    # Weather
    widget.WidgetBox(**base(bg='darker',fg='color2'), 
                    widgets=[widget.Wttr(**base(bg='darker',fg='color2'), location={location:''},fontsize=18,width=550,scroll=True,update_interval=60,format="Feels like %f |  %h | 煮%w | %m%M |   %p |  %P | %c ")],
                    text_closed="",fontsize=18,text_open=" "),
    widget.Wttr(**base(bg='darker',fg='color2'), location={location:''},fontsize=18,format=" %t" , update_interval=60),
    # Check Updates
    # icon(fg="color5", text=' '), # Icon: nf-fa-download
    widget.CheckUpdates(**base(bg='darker',fg='color4'),colour_have_updates=colors['color4'],colour_no_updates=colors['color4'],
                        no_update_string='  0', display_format='  {updates}',fontsize=18,
                        execute=f"echo -e '{password}' | sudo -S sudo powerpill --noconfirm -Su && paru --noconfirm -Su && notify-send -a Updater -i /usr/share/icons/Dracula/scalable/apps/nx-software-updater.svg 'System Updated'",
                        mouse_callbacks={"Button3":lambda:os.system("notify-send -a Updater -i /usr/share/icons/Dracula/scalable/apps/nx-software-updater.svg \"$(pacman -Qu | cut -d \' \' -f 1)\"")}),
    widget.TextBox(**base(fg='darker'),text=" ",fontsize=20.5,padding=-1),

    # System Tray and Notification Control
    widget.TextBox(**base(fg='darker'),text="",fontsize=20.5,padding=-1),
    # Systray
    widget.Systray(**base(bg='darker'), padding=5),
    # DND setting
    widget.GenPollText(**base(bg='darker',fg='light'),fontsize=20,func=dunst,update_interval=1,padding=6,
                       mouse_callbacks={"Button1": toggle_dunst,"Button3": toggle_notif_center}),
    widget.TextBox(**base(fg='darker'),text=" ",fontsize=20.5,padding=-1),
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
    'fontsize': 15,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
