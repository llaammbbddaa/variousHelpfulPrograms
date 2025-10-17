#!/bin/bash

usage() {
	echo "usage: clenter [option]"
	echo "options:"
	echo "  -h		help"
	echo "  -i [index]	set level"
	echo ""
	echo "    index: 0 -> ~/path/to/file$"
	echo "    index: 1 -> file$"
	echo "    index: 2 -> $"
	echo "    index: 3 -> "
	echo "    index: j -> \[\e[1;35m\]\u@\h \[\e[1;33m\]\W\[\e[0m\]\λ "

}

changeView() {

	if [ "$2" == "0" ]; then
		PS1='\w\$ '
	elif [ "$2" == "1" ]; then
		PS1='\W\$ '
	elif [ "$2" == "2" ]; then
		PS1='\$ '
	elif [ "$2" == "3" ]; then
		PS1=''
	elif [ "$2" == "j" ]; then
		# PS1='\[\e[1;35m\]\u@\h \[\e[1;33m\]\W\[\e[0m\]\-> '
		PS1='\[\e[1;34m\]\W -> \[\e[0m\]'
	else
		echo "invalid option"
	fi
}

if [ "$1" == "-i" ]; then
	changeView "$@"
elif [ "$1" == "-h" ]; then
	usage
else
	echo "enter valid flag"
fi
