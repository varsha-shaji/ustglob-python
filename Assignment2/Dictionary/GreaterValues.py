#3.	Write a Python function that takes a dictionary and returns a list of keys that have values greater than 50.
def get_greater_values_keys(input_dict):
    result = []
    for key, value in input_dict.items():
        if value > 50:
            result.append(key)
    return result

data = {"a": 75, "b": 45, "c": 60}
print(get_greater_values_keys(data))

