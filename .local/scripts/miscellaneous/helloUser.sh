#!/bin/bash

# Define ASCII art for A-Z
declare -A art
art[A]="
 _____  
|  _  | 
| |_| | 
|  _  | 
|_| |_| 
"
art[B]="
 ____  
| __ ) 
|  _ \ 
| |_) |
|____/ 
"
art[C]="
  ____ 
 / ___|
| |    
| |___ 
 \____|
"
art[D]="
  ____  
 |  _ \ 
 | | | |
 | |_| |
 |____/ "
art[E]="
  _____ 
 | ____|
 | |__  
 |  __| 
 |_____|
"
art[F]="
  _____ 
 |  ___|
 | |_   
 |  _|  
 |_|    
"
art[G]="
  _____ 
 / ____|
| |  __ 
| | |_ |
 \_____|"
art[H]="
  _    _ 
 | |  | |
 | |__| |
 |  __  |
 |_|  |_|"
art[I]="
  _   
 | |  
 | |  
 | |  
 |_|  
"
art[J]="
      _ 
     | |
  _  | |
 | |_| |
  \___/ "
art[K]="
  _  __ 
 | |/ / 
 | ' /  
 |  <   
 |_|\_\ "
art[L]="
  _      
 | |     
 | |     
 | |____ 
 |______|
"
art[M]="
 __  __  
|  \/  | 
| \  / | 
| |\/| | 
| |  | | 
|_|  |_|"
art[N]="
  _    _ 
 |  \ | |
 |   \| |
 | | \  |
 |_|  \_|"
art[O]="
  ____  
 / __ \ 
| |  | |
| |__| |
 \____/ "
art[P]="
_____  
|  _ \ 
| |_) )
|  _ / 
|_|    "
art[Q]="
  ___    
 / _ \   
| | | |  
| |_| |  
 \___\_\ "
art[R]="
 ____   
 |  _ \ 
 | |_) |
 |    < 
 |_|\_\ "
art[S]="
  _____ 
 / ____|
| (___  
 ____) |
|_____/ "
art[T]="
 _____ 
|_   _|
  | |  
  | |  
  |_|  "
art[U]="
 _    _ 
| |  | |
| |  | |
| |__| |
 \____/ "
art[V]="
__    __
\ \  / /
 \ \/ / 
  \  /  
   \/   "
art[W]="
 _    _ 
| |  | |
| |__| |
|      |
\__/\__/
"
art[X]="
__  __
\ \/ /
 \  / 
 /  \ 
/_/\_\\
"
art[Y]="
 _    _  
\ \  / / 
 \ \/ /  
  \  /   
  /_/    "
art[Z]="
 _____  
|___  | 
   / /  
  / /__ 
 |_____|
"

# Function to print the ASCII art of a name
print_ascii_art() {
    local name="$1"

    # Create a 2D array to hold the ASCII art lines
    local art_lines=()
    
    # Populate the art_lines array with ASCII art
    for ((i=0; i<${#name}; i++)); do
        char=${name:i:1}
        char=$(echo "$char" | tr '[:lower:]' '[:upper:]')
        if [[ ${art[$char]} ]]; then
            # Split the ASCII art into lines
            IFS=$'\n' read -d '' -ra lines <<< "${art[$char]}"
            # Append each line of the character art to the corresponding line in art_lines
            for ((j=0; j<5; j++)); do
                art_lines[$((j))]+="${lines[$j]}  "
            done
        else
            for ((j=0; j<5; j++)); do
                art_lines[$((j))]+="      "  # For characters not in the art dictionary
            done
        fi
    done

    # Print the collected ASCII art lines
    for line in "${art_lines[@]}"; do
        echo "$line"
    done
}

print_ascii_art "Hello $(whoami)"
