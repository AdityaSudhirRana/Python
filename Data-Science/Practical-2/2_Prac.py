print("F105 - Aditya Rana")
# 2a. Create a Nested Tuple
nested_tuple = ((105, "AdityaRana"), (102, "Mohid"), (82, "Charlie"))

print("2a. Nested Tuple")
print(nested_tuple)
print("")



# 2b. Sort a Nested Tuple Using sorted()
sorted_list = sorted(nested_tuple, key=lambda x: x[0])
sorted_tuple = tuple(sorted_list)

print("2b. Sorted Nested Tuple")
print(sorted_tuple)
print("")



# 2c. Copy or Clone a List
original_list = [10, 20, 30, 40]

cloned_list = original_list[:]

print("2c. Copy/Clone a List")
print("Original List:", original_list)
print("Cloned List:  ", cloned_list)
print("Are they separate objects?", original_list is not cloned_list)
print()



# 2d. Check Immutability Property of Tuples
new_tuple = (10, 20, 30)

print("2d. Immutability Check")
print("Attempting to modify index 0 of the tuple...")

try:
    new_tuple[0] = 99
except TypeError as error:
    print(f"Caught expected error: {error}")
    print("Result: Immutability verified. Tuples cannot be modified.")
