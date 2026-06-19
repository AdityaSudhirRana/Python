import math

def calculate_square_roots():
    print("S105 - Aditya Rana")
    print("Square Root Calculator (exit to exit)")
    
    while True:
        user_input = input("\nEnter a number: ")
        
        if user_input == 'exit':
            print("Goodbye")
            break
            
        try:
            number = float(user_input)
            
            if number < 0:
                raise ValueError("Cannot calculate the square root of a negative number.")
            
            result = math.sqrt(number)
            print(f"{number} = {result}")
            
        except ValueError as e:
            print(f"Error: Invalid input! {e}")

calculate_square_roots()
