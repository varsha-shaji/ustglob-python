fruits = ["Apple", "Banana", "Cherry", "Date", "orange", "Cherry"]

search_item = input("Enter the fruit to search: ")
if search_item.capitalize() in fruits:
    print(f"{search_item} is in the list")
else:
    print(f"{search_item} is not in the list")
    