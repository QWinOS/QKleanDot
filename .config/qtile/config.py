from libqtile import hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
import psutil
from details import password

from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    qtile_path = path.join(path.expanduser('~'),".config","qtile")
    subprocess.call(['bash',path.join(qtile_path,'scripts/autostart.sh'),f'{password}'])
    # Uncomment below line to auto mount external drive
    # P.S. change the informations accordingly in mounst.sh
    # before uncommenting
    # subprocess.call([path.join(qtile_path, 'scripts/mount.sh')])


# Window swallowing ;)
@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {
        c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()
    }
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, "parent"):
        window.parent.minimized = False

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'Qtile'
