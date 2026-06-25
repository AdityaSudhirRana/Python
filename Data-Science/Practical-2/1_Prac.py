my_tuple = (10, "AdityaRana", 3.14, True, "Data")
print("1a. Original Tuple")
print(my_tuple)
print()


# 1b. Access the first and last elements using indexing
first_element = my_tuple[0]
last_element = my_tuple[-1]
print("1b. Indexing")
print(f"First element: {first_element}")
print(f"Last element: {last_element}")
print()


# 1c. Slice a tuple and print the middle 3 elements
middle_three = my_tuple[1:4]
print("--- 1c. Slicing Middle 3 Elements ---")
print(middle_three)
print()


# 1d. Concatenate two tuples and print the result
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
concatenated_tuple = tuple_a + tuple_b
print("1d. Concatenation")
print(concatenated_tuple)
print()


# 1e. Reverse a tuple using slicing
reversed_tuple = my_tuple[::-1]
print("1e. Reversed Tuple")
print(reversed_tuple)
print()


# 1f. Count how many times an element appears in a tuple
count_tuple = (1, 2, 3, 2, 4, 2, 5)
to_count = 2
appearance_count = count_tuple.count(to_count)
print("1f. Element Count")
print(f"Tuple: {count_tuple}")
print(f"The element '{to_count}' appears {appearance_count} times.")
print()


# 1g. Find the index of a specific element in a tuple
search_element = "AdityaRana"
element_index = my_tuple.index(search_element)
print("1g. Find Index")
print(f"The index of '{search_element}' is: {element_index}")
print()


# 1h. Check if an element exists in a tuple
check_element = 3.14
exists = check_element in my_tuple
print("1h. Existence Check")
print(f"Does {check_element} exist in the tuple? {exists}")
print()


# 1i. Convert a list to a tuple
my_list = ["apple", "banana", "cherry"]
converted_tuple = tuple(my_list)
print("1i. List to Tuple Conversion")
print(f"Original List: {my_list}")
print(f"Converted Tuple: {converted_tuple}")
print()


# 1j. Sort a tuple of numbers in ascending order
unsorted_tuple = (45, 12, 89, 5, 23)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("1j. Sorting Numbers")
print(f"Unsorted: {unsorted_tuple}")
print(f"Sorted:   {sorted_tuple}")
print()


# 1k. Repeat a tuple 3 times using the * operator
base_tuple = ("A", "B")
repeated_tuple = base_tuple * 3
print("1k. Tuple Repetition")
print(repeated_tuple)
print()


# 1l. Check the immutability property by trying to modify an element
print("1l. Immutability Verification")
print("Attempting to modify the element at index 0...")

try:
    my_tuple[0] = 999
except Exception as e:
    print(f"Caught expected error: {e}")
