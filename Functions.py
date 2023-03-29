from Book_store import admin
from Book_store import staff
from Book_store import books
from Book_store import store
from Book_store import customers

def add_admin(ad_list):
    print(f"Input admin info: /n")
    id = str(input(f"Admin ID: "))
    name = str(input(f"Admin name: "))
    dob = str(input("DoB: "))
    phone = str(input(f"Phone number: "))
    ad_list += [admin.Admin(id, name, dob, phone)]

#For admins:
def input_store_info():
    print(f"Input store infomation: \n")
    id = str(input(f"Store ID: "))
    name = str(input(f"Store name: "))
    address = str(input(f"Address: "))
    phone = str(input(f"Phone number: "))
    new_store = store.Store(id, name, address, phone)
    return new_store
    
def show_store_info(store):
    print(f"Store ID: {store.get_id()} \n"
          f"Store name: {store.get_name()} \n"
          f"Address: {store.get_address()} \n"
          f"Phone number: {store.get_phone()} \n")
    
def add_staff(staff_list):
    n = int(input("Enter number of staffs you want to add: "))
    for i in range(n):
        print(f"\nEnter staff information: ")
        id = str(input(f"Enter staff ID: "))
        name = str(input(f"Staff name: "))
        dob = str(input(f"DoB: "))
        address = str(input("Address: "))
        phone = str(input("Phone number: "))
        staff_list += [staff.Staff(id, name, dob, address, phone)]
        
def set_staff_salary(staff_list):
    for i in range(len(staff_list)):
        salary = int(input(f"\nSalary for staff {staff_list[i].get_name()} (VND/month): "))
        staff_list[i].set_salary(salary)
        
        
def show_staff(staff_list): #include salary
    print(f"All staffs information: \n")
    for i in range(len(staff_list)):
        print(f"    Staff ID: {staff_list[i].get_id()} \n"
              f"    Name: {staff_list[i].get_name()} \n"
              f"    DoB: {staff_list[i].get_dob()} \n"
              f"    Address: {staff_list[i].get_addr()} \n"
              f"    Phone number: {staff_list[i].get_phone_num()} \n"
              f"    Salary (VND/month): {staff_list[i].get_salary()} \n\n")
    
def show_books(book_list): #include price
    for i in range(len(book_list)):
        print(f"\nBook ID: {book_list[i].get_id()} \n"
              f"Title: {book_list[i].get_title()} \n"
              f"Genre: {book_list[i].get_genre()} \n"
              f"Author: {book_list[i].get_author()} \n"
              f"Year of publication: {book_list[i].get_pub_year()} \n"
              f"Target audience: {book_list[i].get_target()} \n"
              f"Price: {book_list[i].get_price()} \n\n")
    
    
def find_books_index(book_list): #by name
    name = str(input("Enter book name: "))
    for i in range(len(book_list)):
        if book_list[i].get_name() == name:
            return i
    if i >= len(book_list):
        print("Book does not exist!")
        return None


def find_staff_index(staff_list): #by name
    nm = str("Enter staff name you want to find: ")
    for i in range(len(staff_list)):
        if staff_list[i].get_name() == nm:
            return i
    if i>= len(staff_list):
        print(f"Can't find staff!")
        return None
    
    
def modify_staff_info(i):
    

#For staffs:
def input_books(books_list):
    n = int(input(f"Enter number of books to add: "))
    for i in range(n):
        id = str(input(f"Book ID: "))
        title = str(input(f"Title: "))
        genre = str(input(f"Genre: "))
        author = str(input(f"Author: "))
        year = str(input(f"Year of publication: "))
        quantity = int(input(f"Stock: "))
        new_book = books.Book(id, title, genre, author, year, quantity)
        new_book.set_target()
        new_book.set_price()
        books_list += [new_book]
    
    
def show_books(book_list): #include price
    for i in range(len(book_list)):
        print(f"\nBook ID: {book_list[i].get_id()} \n"
              f"Title: {book_list[i].get_title()} \n"
              f"Genre: {book_list[i].get_genre()} \n"
              f"Author: {book_list[i].get_author()} \n"
              f"Year of publication: {book_list[i].get_pub_year()} \n"
              f"Target audience: {book_list[i].get_target()} \n"
              f"Price: {book_list[i].get_price()} \n\n")
        
    def find_books_index(book_list): #by name
    name = str(input("Enter book name: "))
    for i in range(len(book_list)):
        if book_list[i].get_name() == name:
            return i
    if i >= len(book_list):
        print("Book does not exist!")
        return None
    
def modify_book_info(i)


def show_store_info(store):
    print(f"Store ID: {store.get_id()} \n"
          f"Store name: {store.get_name()} \n"
          f"Address: {store.get_address()} \n"
          f"Phone number: {store.get_phone()} \n")


def add_customer(customers_list):


def show_customer(customers_list):    

#Need function to validate input   






