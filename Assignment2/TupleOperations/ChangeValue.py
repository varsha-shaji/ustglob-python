#4.	Given the tuple t = (1, 2, 3, 4), how can you change the value 3 to 100?
t=(1, 2, 3, 4)
lst=list(t) #since tuples are immutable, convert to list
lst[2]=100
t=tuple(lst) #convert back to tuple
print("Updated tuple:", t)