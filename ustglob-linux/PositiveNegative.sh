read -p "Enter a number : " a
function PositiveNegative(){

	if [ $a -gt 0 ] ; then
		echo "$a is a Positive Number "
	elif [ $a -lt 0 ]; then
		echo "$a is a  Negative Number"
	else
		echo "Given Number is Zero"

	fi
}

PositiveNegative


