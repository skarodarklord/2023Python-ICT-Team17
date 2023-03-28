from Book_store import admin
from Book_store import staff
from Book_store import books


def add_admin(ad_list):
    print(f"Input admin info: /n")
    i = str(input(f"Admin ID: "))
    n = str(input(f"Admin name: "))
    d = str(input("DoB: "))
    p = str(input(f"Phone number: "))
    ad_list += [admin.admin(i, n, d, p)]

#For admins:
def input_store_info():
def show_store_info(store):
def add_staff(staff_list):
def set_staff_salary(staff_list):
def show_staff(staff_list):
def show_books(book_list): #include price
    
#For staffs:
def input_books(books_list):
def input_book_price(book_list):
def show_books(book_list): #include price
def show_store_infos(store):
def add_customer(customers_list):
def show_customer(customers_list):    

    






print(f"What are you? \n"
      f"1. Admin \n"
      f"2. Staff \n")
op = int(input(f"Your choice: "))
match op:
    case 1:
        print(f"What do you want? ")
        
    case 2:
        print(f"What do you want?")
        
    case _:
        print(f"Invalid choice!")