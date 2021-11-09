# Qtile keybindings
from libqtile.config import Key
from libqtile.command import lazy
from settings.path import *
from os import path

mod = "mod4"
keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # ---------- Scratchpad & Dropdown ------------
    (["control", "shift"], "F11", lazy.group["scratchpad"].dropdown_toggle('ter')),
    (["control", "shift"], "F12", lazy.group["scratchpad"].dropdown_toggle('calc')),
    (["control", "shift"], "F10", lazy.group["scratchpad"].dropdown_toggle('clip')),

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),

    # ------------ App Configs ------------

    # Menu
    (["mod1"], "space", lazy.spawn(path.join(rofi_path, 'colorful/launcher.sh'))),

    # Power Menu
    # (["mod1"], "Tab", lazy.spawn(path.join(rofi_path, 'text/launcher.sh'))),
    (["mod1"], "p", lazy.spawn(path.join(rofi_path, 'powermenu/powermenu.sh'))),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),
    # ([mod], "b", lazy.spawn("vieb")),

    # Text Editor
    ([mod], "t", lazy.spawn("code")),
    
    # File Explorer
    ([mod], "e", lazy.spawn("pcmanfm -n")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    # ([mod], "r", lazy.spawn("redshift -O 4500")),
    # ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),
    # Media player controls
    ([], "XF86AudioPlay", lazy.spawn("/usr/bin/playerctl play-pause")),
    # ([], "XF86AudioPause", lazy.spawn("/usr/bin/playerctl pause")),
    ([], "XF86AudioNext", lazy.spawn("/usr/bin/playerctl next")),
    ([], "XF86AudioPrev", lazy.spawn("/usr/bin/playerctl previous")),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
