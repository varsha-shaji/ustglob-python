read -p "Enter a number : " n
SumofN(){
	sum=0
	for (( i=1;i<=n;i++ ))
	do
		sum=$((sum+i))
	done
	echo "Sum of numbers from 1 to $n =$sum"
}
SumofN
