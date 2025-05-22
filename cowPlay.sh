#!/bin/bash
clear
path="$HOME/to/path/" # enter appropriate path, ex: "$HOME/Music/jams"
song="$(find "$path" -type f | shuf -n 1)"
cowsay "playing ${song}"
cvlc "${song}"
