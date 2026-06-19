def swap_elements_in_list(lst, index1, index2):
    print(f"Original List: {lst}")
    
    try:
        lst[index1], lst[index2] = lst[index2], lst[index1]
        
        print(f"Swapped index {index1} with index {index2} successfully.")
        print(f"Updated List:  {lst}")
        
    except IndexError:
        print(f"Error: One or both indices ({index1}, {index2}) are out of range for this list.")


my_list = ["Apple", "Banana", "Cherry", "Mango", "Lichi"]

swap_elements_in_list(my_list, 1, 4)
