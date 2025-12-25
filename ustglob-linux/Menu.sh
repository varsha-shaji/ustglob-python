add() {
    echo "Result = $(($1 + $2))"
}

sub() {
    echo "Result = $(($1 - $2))"
}

mul() {
    echo "Result = $(($1 * $2))"
}

div() {
    if [ $2 -eq 0 ]; then
        echo "Division by zero is not allowed"
    else
        echo "Result = $(($1 / $2))"
    fi
}

while true
do
    echo "----- MENU -----"
    echo "1. Add"
    echo "2. Subtract"
    echo "3. Multiply"
    echo "4. Divide"
    echo "5. Exit"
    read -p "Enter your choice: " choice

    if [ $choice -eq 5 ]; then
        echo "Exiting..."
        break
    fi

    read -p "Enter first number: " a
    read -p "Enter second number: " b

    case $choice in
        1) add $a $b ;;
        2) sub $a $b ;;
        3) mul $a $b ;;
        4) div $a $b ;;
        *) echo "Invalid choice" ;;
    esac
done
