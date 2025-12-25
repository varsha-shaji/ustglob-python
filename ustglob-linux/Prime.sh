read -p "Enter a number : " n
prime(){
  if (( n<=1 )); then
     echo "$n is not a prime number"
     return
  fi
  for (( i=2;i<n;i++ ))
  do
	if (( n%i ==0 )); then
	   echo "$n is not a prime number"
	   return
	fi
  done
  echo "$n is a prime number"
}

prime
