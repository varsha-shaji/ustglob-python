fruits = ["Apple", "Banana", "Cherry", "Date", "orange", "Cherry","Apple"]

def remove_duplicates():
    removed = []
    for i in fruits:
        if fruits.count(i) > 1:
            fruits.remove(i)
            removed.append(i)
    print("Removed duplicate elements:", removed)

remove_duplicates()
print("After duplicates removed:", fruits)
