my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

# 1. Mutability
my_list.append(4)      # Allowed
# my_tuple.append(4)   #  Not allowed

# 2. Reassignment
my_list[1] = 200       # Allowed
# my_tuple[1] = 200    # Not allowed

print("List:", my_list)
print("Tuple:", my_tuple)
