read -p "Enter a number : " n
factorial(){
	f=1
	i=1
	while [ $i -le $n ]
	do
		f=$((f*i))
		i=$((i+1))

	done
	echo "Factorial of $n = $f"
	
}

factorial n
