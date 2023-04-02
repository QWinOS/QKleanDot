# Qtile keybindings
from libqtile.config import Key
from libqtile.command import lazy

def show_keys():
    key_help = ""
    for k in keys:
        mods = ""
        for m in k.modifiers:
            if m == "mod4":
                mods += "Win + "
            elif m == "mod1":
                mods += "Alt + "
            else:
                mods += m.capitalize() + " + "
        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key
        key_help += "{:<30} {}".format(mods, k.desc + "\n")
    return key_help

mod = "mod4"
keys = [
    # ---------- Scratchpad & Dropdown ------------
    Key([mod, "control"], "d", lazy.group["scratchpad"].dropdown_toggle('ter'),desc="Toggle floating terminal"),
    Key([], "XF86Calculator", lazy.group["scratchpad"].dropdown_toggle('calc'),desc="Toggle floating calculator"),
    Key([mod, "control"], "m", lazy.group["scratchpad"].dropdown_toggle('calc'),desc="Toggle floating calculator"),
    Key([mod, "control"], "F10", lazy.group["scratchpad"].dropdown_toggle('clip'),desc="Toggle floating clipboard"),

    # ------------ Window Configs ------------
    # Switch between windows in current stack pane
    Key([mod], "j", lazy.layout.down(),desc="Move focus down"),
    Key(["mod1"], "Tab", lazy.layout.down(),desc="Move focus to next window"),
    Key([mod], "k", lazy.layout.up(),desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(),desc="Move focus left"),
    Key([mod], "l", lazy.layout.right(),desc="Move focus right"),

    # Change window sizes
    Key([mod, "control"], "l", lazy.layout.grow(),desc="Resize window right"),
    Key([mod, "control"], "h", lazy.layout.shrink(),desc="Resize window left"),
    Key([mod, "control"], "n", lazy.layout.normalize(),desc="Normalize window size ratios"),

    # Window States
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(),desc="Toggle fullscreen"),
    Key([mod], "f", lazy.window.toggle_floating(),desc="Toggle floating on focused window"),
    Key([mod], "m", lazy.window.toggle_minimize(),desc="Toggle minimization on focused window"),
    Key([mod, "shift"], "m", lazy.group.unminimize_all(),desc="Unminimize all windows in current group"),

    # Floating controls
    Key([mod], "bracketleft", lazy.group.prev_window(),lazy.window.bring_to_front(),desc="Cycle previous floating window"),
    Key([mod], "bracketright", lazy.group.next_window(),lazy.window.bring_to_front(),desc="Cycle next floating window"),

    # Move windows in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),desc="Move window right"),
    Key([mod], "s", lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(),desc="Toggle forward layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(),desc="Toggle last layout"),

    Key([mod], "q", lazy.window.kill(),desc="Kill active window"),

    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(),desc="Toggle floating calculator"),
    Key([mod], "comma", lazy.prev_screen(),desc="Toggle floating calculator"),

    # ------------ Qtile Options ------------
    Key([mod, "control"], "r", lazy.restart(),desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),desc="Shutdown Qtile"),

    # ------------ App Configs ------------
    Key([mod], "p", lazy.spawn("./.config/rofi/powermenu/powermenu.sh"),desc="Launch powermenu"),
    Key([mod], "b", lazy.spawn("firefox"),desc="Launch browser"),
    Key([mod], "t", lazy.spawn("code"),desc="Launch text editor"),
    Key([mod], "Return", lazy.spawn("alacritty"),desc="Launch Alacritty Terminal"),

    # ------------ Miscellaneous ------------
    Key(["mod1"], "space", lazy.spawn("./.config/rofi/centerConsole/launchConsole.sh --launcher"),desc="Open app launcher"),
    Key(["mod1", "control"], "space", lazy.spawn("./.config/rofi/centerConsole/launchConsole.sh --search"),desc="Open google search"),
    #Key([mod], "b", lazy.spawn("./.config/eww/scripts/toggle_eww.sh"),desc="Toggle bottom eww bar visibility"),
    Key([mod, "shift"], "b", lazy.spawn("qtile cmd-obj -o cmd -f hide_show_bar"),desc="Toggle visibility of qtile bar"),
    Key([mod, "control"], "w", lazy.spawn("./.local/bin/nc_flash_window"),desc="Flash currently focused window"),
    Key([], "Print", lazy.spawn("maim Pictures/$(date\ +%s).jpg"),desc="Take screenshot"),
    Key([mod,"shift"], "p", lazy.spawn("./.config/picom/scripts/togglepicom"),desc="Toggle Picom Compositor"),
    Key([mod,"shift"], "c", lazy.spawn("./.local/scripts/miscellaneous/colorpick.sh"),desc="Open color picker"),
    Key([mod,"control"], "c", lazy.spawn("./.config/dunst/scripts/dunst.sh --toggle"),desc="Toggle dunst notification service"),
    Key([mod], "a", lazy.spawn("./.config/dunst/scripts/dunst.sh --notif-center"),desc="Open notification center"),
    Key([mod], "Escape", lazy.spawn("./.local/scripts/screen/lockinLogout/screenlock --no-suspend"),desc="Lock screen"),
    
    # ------------ Hardware Configs ------------
    # Volume
    Key([], "XF86AudioRaiseVolume", lazy.spawn("./.config/eww/scripts/vol.sh up"),desc="Increase Volume"),
    Key([mod], "F8", lazy.spawn("./.config/eww/scripts/vol.sh up"),desc="Increase Volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("./.config/eww/scripts/vol.sh down"),desc="Decrease Volume"),
    Key([mod], "F7", lazy.spawn("./.config/eww/scripts/vol.sh down"),desc="Decrease Volume"),
    Key([], "XF86AudioMute", lazy.spawn("./.config/eww/scripts/vol.sh mute"),desc="Toggle Mute"),
    Key([mod], "F6", lazy.spawn("./.config/eww/scripts/vol.sh mute"),desc="Toggle Mute"),

    # Mic Volume
    Key([mod], "XF86AudioRaiseVolume", lazy.spawn("./.config/eww/scripts/micvol.sh up"),desc="Increase mic volume"),
    Key([mod,"control"], "F8", lazy.spawn("./.config/eww/scripts/micvol.sh up"),desc="Increase mic volume"),
    Key([mod], "XF86AudioLowerVolume", lazy.spawn("./.config/eww/scripts/micvol.sh down"),desc="Decrease  mic volume"),
    Key([mod,"control"], "F7", lazy.spawn("./.config/eww/scripts/micvol.sh down"),desc="Decrease  mic volume"),
    Key([mod], "XF86AudioMute", lazy.spawn("./.config/eww/scripts/micvol.sh mute"),desc="Toggle mic Mute"),
    Key([mod,"control"], "F6", lazy.spawn("./.config/eww/scripts/micvol.sh mute"),desc="Toggle mic Mute"),

    # Media player controls
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"),desc="Play previous media"),
    Key([mod], "F9", lazy.spawn("playerctl previous"),desc="Play previous media"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"),desc="Toggle play/pause media"),
    Key([mod], "F10", lazy.spawn("playerctl play-pause"),desc="Toggle play/pause media"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"),desc="Play next media"),
    Key([mod], "F11", lazy.spawn("playerctl next"),desc="Play next media"),
    Key([mod], "F12", lazy.spawn("playerctl stop"),desc="Stop media"),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("./.config/eww/scripts/bright.sh up"),desc="Increase Screen Brightness"),
    Key([mod], "F3", lazy.spawn("./.config/eww/scripts/bright.sh up"),desc="Increase Screen Brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("./.config/eww/scripts/bright.sh down"),desc="Decrease Screen Brightness"),
    Key([mod], "F2", lazy.spawn("./.config/eww/scripts/bright.sh down"),desc="Decrease Screen Brightness"),
]

keys.extend([Key([mod],"grave",lazy.spawn(
    "sh -c 'echo \""+ show_keys()+'" | rofi -dmenu -theme ~/.config/rofi/configTall.rasi -i -p ">"\''),desc="View key bindings")])

