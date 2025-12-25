read -p "Enter a number : " n
rev=0
while (( n!=0 ))
do 
  r=$(( n%10 ))
  rev=$(( rev*10+r ))
  n=$(( n/10 ))
done
echo "Reversed Number = $rev"
