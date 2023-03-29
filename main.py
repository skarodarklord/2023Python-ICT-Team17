print(f"What are you? \n"
      f"1. Admin \n"
      f"2. Staff \n")
op = int(input(f"Your choice: "))
match op:
    case 1:
        print(f"What do you want? \n")
        
    case 2:
        print(f"What do you want? \n")
        
    case _:
        print(f"Invalid choice!")