#5.	Write a Python function that merges two dictionaries.
def merge_dictionaries(dict1, dict2):   
    return {**dict1, **dict2}
dict1={'a': 1, 'b': 2}
dict2={"b": 2,"c":4}
merged_dict = merge_dictionaries(dict1, dict2)
print("Dict1",dict1)
print("Dict2",dict2)
print("Merged Dictionary",merged_dict)