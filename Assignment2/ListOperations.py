fruits=["Apple","Banana","Cherry","Date","orange","Cherry"]

# 1. Add an item to the end of the list using append() method
fruits.append("kiwi")
print(fruits)


# 2. Remove an element from the list by its index
fruits.pop(2)
print(fruits)

# 3. output of following snippet

lst = [1, 2, 3, 4, 5]
lst[1:3] = [10, 20]
print(lst)


# 4. check if an element exists in a list in Python
search_item = input("Enter the fruit to search: ")
if search_item.capitalize() in fruits:
    print(f"{search_item} is in the list")
else:
    print(f"{search_item} is not in the list")
    
    
# 5. Python function that removes duplicates from a list without using the set() function.
def remove_duplicates():
    for i in fruits:
        while fruits.count(i) > 1:
            fruits.remove(i)
            
            
remove_duplicates()
print(fruits)