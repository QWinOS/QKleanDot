#!/usr/bin/env bash
theme="style"
dir="$HOME/.config/rofi/centerConsole"

# dark
ALPHA="#00000000"
BG="#000000ff"
FG="#FFFFFFff"
SELECT="#101010ff"

# light
# ALPHA="#00000000"
# BG="#FFFFFFff"
# FG="#000000ff"
# SELECT="#f3f3f3ff"

# accent colors
COLORS=('#EC7875' '#61C766' '#FDD835' '#42A5F5' '#BA68C8' '#4DD0E1' '#00B19F' \
		'#FBC02D' '#E57C46' '#AC8476' '#6D8895' '#EC407A' '#B9C244' '#6C77BB')
ACCENT="${COLORS[$(( $RANDOM % 14 ))]}ff"

# overwrite colors file
cat > $dir/colors.rasi <<- EOF
	/* colors */

	* {
	  al:  $ALPHA;
	  bg:  $BG;
	  se:  $SELECT;
	  fg:  $FG;
	  ac:  $ACCENT;
	}
EOF

# setting up search engine
# Will need to update usr/lib/node_modules/rofi-search/rofi-search when rofi-search updates to change default prompt

#export ROFI_SEARCH='googler'
#export GOOGLE_ARGS='["--count", 13]'
#export GOOGLE_API_KEY='AIzaSyCrJ4mbG-TrR0_VxaqM9rOzknhIAiCvDwc'
export GOOGLE_API_KEY='AIzaSyCCCEcI_cQgi1DrWcsM0nojQ5LpqubtoLc'
#export GOOGLE_SEARCH_ID='b84e8a9005e8ce3b4'
export GOOGLE_SEARCH_ID='254dfc85597e64312'
export ROFI_SEARCH='cse'

export TITLE_COLOR='#5e81ac'
export ROFI_SEARCH_CMD='~/.local/scripts/miscellaneous/linkhandler $URL'

# comment these lines to disable random style
# themes=($(ls -p --hide="launcher.sh" --hide="colors.rasi" $dir))
# theme="${themes[$(( $RANDOM % 12 ))]}"

case "$1" in
  --launcher|-l)
    rofi -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
    ;;
  --search|-s)
    rofi -modi blocks -blocks-wrap /usr/bin/rofi-search -show blocks -lines 13 -eh 4 -kb-custom-1 'Control+y' -theme ~/.config/rofi/centerConsole/style.rasi  
    ;;
esac
