def calculate_total():
    print("S105 - Aditya Rana")
    
    user_input = input("Enter numbers: ")
    
    string_list = user_input.split()
    
    numbers_list = [float(num) for num in string_list]
    
    total_sum = sum(numbers_list)
    
    print(f" Your List: {numbers_list}")
    print(f" Total Sum: {total_sum}")

calculate_total()
