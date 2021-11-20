# Qtile workspaces
from libqtile.dgroups import simple_key_binder
from libqtile.config import Key, Group, ScratchPad, DropDown
from libqtile.command import lazy
from settings.keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons:
# nf-fa-firefox,
# nf-fae-python,
# nf-dev-terminal,
# nf-fa-code,
# nf-seti-config,
# nf-mdi-folder,
# nf-mdi-image,
# nf-fa-video_camera,
# nf-mdi-layers

# groups = [Group(i) for i in [
#     "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",
# ]
# ]

groups = (
    Group('1', label=' 1 ', layout='monadtall'),
    Group('2', label=' 2 ', layout='monadtall'),
    Group('3', label=' 3 ', layout='monadtall'),
    Group('4', label=' 4 ', layout='ratiotile'),
    Group('5', label=' 5 ', layout='ratiotile'),
    Group('6', label=' 6 ', layout='ratiotile'),
    Group('7', label=' 7 ', layout='bsp'),
    Group('8', label=' 8 ', layout='bsp'),
    Group('9', label=' 9 ', layout='max'),
    Group('0', label=' 0 ', layout='max'),
    ScratchPad('scratchpad', [
        DropDown(
            'ter', "alacritty", width=0.9, height=0.9, x=0.05, y=0.05, opacity=1.0, on_focus_lost_hide=True),
        DropDown(
            'calc', "alacritty -e bc", width=0.9, height=0.9, x=0.05, y=0.05, opacity=1.0, on_focus_lost_hide=True),
        DropDown(
            'clip', "copyq show", width=0.9, height=0.9, x=0.05, y=0.05, opacity=1.0, on_focus_lost_hide=True)
    ])
)

for i, group in enumerate(groups[:-1], 1):
    # Switch to another group
    keys.append(Key([mod], str(i%10), lazy.group[group.name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i%10), lazy.window.togroup(group.name)))


# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen()),
#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
#     ])


# for i, group in enumerate(groups):
#     actual_key = str(i + 1)
#     keys.extend([
#         # Switch to workspace N
#         Key([mod], actual_key, lazy.group[group.name].toscreen()),
#         # Send window to workspace N
#         Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
#     ])
