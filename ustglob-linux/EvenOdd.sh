check_even_odd(){
	if[ (($1 % 2)) -eq 0 ]; then
		echo "$1 is a even number"
	else
		echo "$1 is an odd number"
	fi
}

check_even_odd 12


