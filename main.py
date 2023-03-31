import Functions

admin_list = []
staff_list = []
book_list = []
customers_list = []
store = None

Functions.add_admin(admin_list)


print(f"What are you? \n"
      f"1. Admin \n"
      f"2. Staff \n")
op1 = int(input(f"Your choice: "))
match op1:
    case 1:
        print(f"Ok Assmin, what do you want? \n"
              f"1. Input store information \n"
              f"2. Show store info \n"
              f"3. Add staff \n"
              f"4. Show staff list \n"
              f"5. Remove staff \n"
              f"6. Update staff information \n"
              f"7. Show book list \n")
        op2 = int(input(f"Choice: "))
        match op2:
            case 1:
                store = Functions.input_store_info()
            case 2:
                Functions.show_store_info(store)
            case 3: 
                Functions.add_staff(staff_list)
                Functions.set_staff_salary(staff_list)
            case 4:
                Functions.show_staff(staff_list)
            case 5:
                Functions.add_staff(staff_list)
                Functions.set_staff_salary(staff_list)
                i = Functions.find_staff_index(staff_list)
                Functions.remove_staff(staff_list, i)
                Functions.show_staff(staff_list)
            case 6: 
                Functions.add_staff(staff_list)
                Functions.set_staff_salary(staff_list)
                i = Functions.find_staff_index(staff_list)
                Functions.modify_staff_info(staff_list, i)
                Functions.show_staff(staff_list)
            case 7: 
                Functions.show_books(book_list)
                
                
    case 2:
        print(f"Ok staff, what do you want? \n")
        
    case _:
        print(f"Invalid choice!")