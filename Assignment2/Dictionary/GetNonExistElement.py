#2.	What happens if you try to access a key that does not exist in a dictionary?
my_dict = {'x': 10, 'y': 20}
print("Original dictionary:", my_dict)
#value=my_dict['z'] #this will raise a KeyError
value=my_dict.get('z') #using get
print(value)