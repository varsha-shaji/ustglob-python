read -p "Enter file name: " file

if [ ! -e "$file" ]; then
    echo "File does not exist"
    exit 1
fi

missing=0

[ -r "$file" ] || { echo "Read permission NOT available"; missing=1; }
[ -w "$file" ] || { echo "Write permission NOT available"; missing=1; }
[ -x "$file" ] || { echo "Execute permission NOT available"; missing=1; }

if [ "$missing" -eq 0 ]; then
    echo "All permissions are available"
fi
