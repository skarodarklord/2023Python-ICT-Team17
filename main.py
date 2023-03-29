import Functions

admin_list = []
staff_list = []
book_list = []
customers_list = []

print(f"What are you? \n"
      f"1. Admin \n"
      f"2. Staff \n")
op1 = int(input(f"Your choice: "))
match op1:
    case 1:
        print(f"Ok Assmin, what do you want? \n")
        
    case 2:
        print(f"Ok staff, what do you want? \n")
        
    case _:
        print(f"Invalid choice!")