# 2a. Find the largest number in a list
numbers_list = [23, 89, 45, 12, 76, 5]
largest_number = max(numbers_list)
print("2a. Largest Number")
print(f"List: {numbers_list}")
print(f"largest number: {largest_number}")
print()


# 2b. Remove duplicates from a list
duplicate_list = [10, 20, 10, 30, 20, 40, 50, 40]
unique_list = list(set(duplicate_list))
print("2b. Remove Duplicates")
print(f"List: {duplicate_list}")
print(f"Removed dupplicates: {unique_list}")
print()


# 2c. Count how many even numbers are in a list
mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = len([num for num in mixed_numbers if num % 2 == 0])
print("2c. Count Even Numbers")
print(f"List: {mixed_numbers}")
print(f"Even numbers: {even_count}")
print()


# 2d. Input 5 numbers and store them in a list, then display the lidt
print("2d. User Input to List")
user_numbers = []
print("Please enter 5 numbers:")
for i in range(1, 6):
    user_input = float(input(f"Enter number {i}: "))
    user_numbers.append(user_input)
print(f"Your collected list: {user_numbers}")
print()


# 2e. Function that returns the average of all numbers in a list
def calculate_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

average_result = calculate_average(user_numbers)
print("2e. List Average Function ---")
print(f"Average of the {user_numbers} is: {average_result:.2f}")
print()


# 2f. Convert a string into a list of characters using list()
sample_string = "DSPython"
char_list = list(sample_string)
print("2f. String to List of Characters")
print(f"Original String: '{sample_string}'")
type(sample_string)
print(f"Character List:  {char_list}")
type(char_list)
print()


# 2g. Join all elements of a list into a single string using join()
word_list = ["My", "Name", "is", "Aditya", "Rana"]
joined_string = "_".join(word_list)
print("2g. Join List into String")
print(f"List: {word_list}")
print(f"Joined String: '{joined_string}'")
