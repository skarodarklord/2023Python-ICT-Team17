from Book_store import admin
from Book_store import staff
from Book_store import books
from Book_store import store
from Book_store import customers

def add_admin(ad_list):        #OK
    print(f"Input admin info: \n")
    id = str(input(f"Admin ID: "))
    name = str(input(f"Admin name: "))
    dob = str(input("DoB: "))
    phone = str(input(f"Phone number: "))
    ad_list += [admin.Admin(id, name, dob, phone)]

#For admin:
def input_store_info():         #OK
    print(f"Input store infomation: \n")
    id = str(input(f"Store ID: "))
    name = str(input(f"Store name: "))
    address = str(input(f"Address: "))
    phone = str(input(f"Phone number: "))
    new_store = store.Store(id, name, address, phone)
    return new_store
    
def show_store_info(store):             #OK
    print(f"Store ID: {store.get_id()} \n"
          f"Store name: {store.get_name()} \n"
          f"Address: {store.get_address()} \n"
          f"Phone number: {store.get_phone()} \n")
    
def add_staff(staff_list):              #OK
    n = int(input("Enter number of staffs you want to add: "))
    for i in range(n):
        print(f"\nEnter staff information: ")
        id = str(input(f"Enter staff ID: "))
        name = str(input(f"Staff name: "))
        dob = str(input(f"DoB: "))
        address = str(input("Address: "))
        phone = str(input("Phone number: "))
        staff_list += [staff.Staff(id, name, dob, address, phone)]
        
def set_staff_salary(staff_list):           #OK
    for i in range(len(staff_list)):
        salary = int(input(f"\nSalary for staff {staff_list[i].get_name()} (VND/month): "))
        staff_list[i].set_salary(salary)
        
def show_staff(staff_list): #include salary             #OK
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

def find_staff_index(staff_list): #by name                  #OK
    nm = str(input(f"Enter staff name you want to find: "))
    for i in range(len(staff_list)):
        if staff_list[i].get_name() == nm:
            return i
    if i>= len(staff_list):
        print(f"Can't find staff!")
        return None
    
def remove_staff(staff_list, i):                        #OK
    staff_list.remove(staff_list[i])
    
def modify_staff_info(staff_list, i):                   #OK
    print(f"What do you want to update? \n"
          f"1. Staff ID \n"
          f"2. Staff name \n"
          f"3. Staff DoB \n"
          f"4. Staff address \n"
          f"5. Staff phone number \n"
          f"6. Staff salary \n")
    op = int(input("Your choice: "))
    match op: 
        case 1:
            print(f"Current staff ID: {staff_list[i].get_id()} \n")
            new_id = str(input(f"New staff ID: "))
            staff_list[i].set_id(new_id)
        case 2: 
            print(f"Current staff name: {staff_list[i].get_name()} \n")
            new_name = str(input(f"New staff name: "))
            staff_list[i].set_name(new_name)
        case 3:
            print(f"Current staff dob: {staff_list[i].get_dob()} \n")
            new_dob = str(input(f"New staff dob: "))
            staff_list[i].set_dob(new_dob)
        case 4:
            print(f"Current staff address: {staff_list[i].get_addr()} \n")
            new_addr = str(input(f"New staff address: "))
            staff_list[i].set_addr(new_addr)
        case 5:
            print(f"Current staff phone number: {staff_list[i].get_phone_num()} \n")
            new_phone = str(input(f"New staff phone number: "))
            staff_list[i].set_phone(new_phone)
        case 6:
            print(f"Current staff salary: {staff_list[i].get_salary()} \n")
            new_salary = str(input(f"New staff salary: "))
            staff_list[i].set_salary(new_salary)
        case _:
            print(f"Invalid choice!")
    

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
    
def modify_book_info(book_list, i):
    print(f"What do you want to modify? \n"
          f"1. Book ID \n"
          f"2. Book title \n"
          f"3. Genre \n"
          f"4. Author \n"
          f"5. Year of publication \n"
          f"6. Quantity \n"
          f"7. Target audience \n"
          f"8. Price \n")
    op = int(input(f"your choice: "))
    match op:
        case 1:
            print(f"Current book ID: {book_list[i].get_id()} \n")
            new_id = str(input(f"Enter new ID: "))
            book_list[i].set_id(new_id)
        case 2:
            print(f"Current book title: {book_list[i].get_title()} \n")
            new_title = str(input(f"Enter new title: "))
            book_list[i].set_title(new_title)
        case 3:
            print(f"Current book genre: {book_list[i].get_genre()} \n")
            new_genre = str(input(f"Enter new genre: "))
            book_list[i].set_genre(new_genre)
        case 4:
            print(f"Current book author: {book_list[i].get_author()} \n")
            new_author = str(input(f"Enter new author: "))
            book_list[i].set_author(new_author)
        case 5:
            print(f"Current book publish year: {book_list[i].get_pub_year()} \n")
            new_year = str(input(f"Enter new publish year: "))
            book_list[i].set_year(new_year)
        case 6:
            print(f"Current book quantity: {book_list[i].get_quantity()} \n")
            new_qu = str(input(f"Enter new quantity: "))
            book_list[i].set_quantity(new_qu)
        case 7:
            print(f"Current book target audience: {book_list[i].get_target()} \n")
            book_list[i].set_target()
        case 8:
            print(f"Current book price: {book_list[i].get_price()} \n")
            book_list[i].set_price()  
        case _: 
            print(f"Invalid choice!")      
            

def show_store_info(store):
    print(f"Store ID: {store.get_id()} \n"
          f"Store name: {store.get_name()} \n"
          f"Address: {store.get_address()} \n"
          f"Phone number: {store.get_phone()} \n")

def add_customer(customers_list):
    n = int(input(f"Enter number of customer you want to add: "))
    for i in range(n):
        id = str(input(f"Enter customer ID: "))
        name = str(input(f"Enter customer name: "))
        dob = str(input(f"Enter customer DoB: "))
        addr = str(input(f"Enter customer address: "))
        phone = str(input(f"Enter customer phone number: "))
        new_customer = customers.Customer(id, name, dob, addr, phone)
        customers_list += [new_customer]

def show_customer(customers_list): 
    for i in range(len(customers_list)):
        print(f"\nCustomer ID: {customers_list[i].get_id()} \n"
              f"Customer name; {customers_list[i].get_name()} \n"
              f"DoB: {customers_list[i].get_dob()} \n"
              f"Address: {customers_list[i].get_addr()} \n"
              f"Phone number: {customers_list[i].get_phonre_num()} \n")
    
def find_customer_index(customers_list):  #by name 
    nm = str(input(f"Enter customer name to find: "))
    for i in range(len(customers_list)):
        if customers_list[i].get_name() == nm:
            return i
    if i >= len(customers_list):
        print(f"Can't find customer!")
        return None
    
def modify_customer_info(customers_list, i): 
    print(f"What do you want to update? \n"
          f"1. Customer ID \n"
          f"2. Customer name \n"
          f"3. Customer DoB \n"
          f"4. Customer address \n"
          f"5. Customer phone number \n")
    op = int(input(f"Your choice: "))
    match op: 
        case 1:
            print(f"Current customer ID: {customers_list[i].get_id()}")
            new_id = str(input('Enter new customer ID: '))
            customers_list[i].set_id(new_id)
        case 2:
            print(f"Current customer name: {customers_list[i].get_name()}")
            new_name = str(input('Enter new customer name: '))
            customers_list[i].set_name(new_name)
        case 3:
            print(f"Current customer dob: {customers_list[i].get_dob()}")
            new_dob = str(input('Enter new customer dob: '))
            customers_list[i].set_dob(new_dob)
        case 4:
            print(f"Current customer address: {customers_list[i].get_addr()}")
            new_addr = str(input('Enter new customer address: '))
            customers_list[i].set_addr(new_addr)
        case 5:
            print(f"Current customer Phone number: {customers_list[i].get_phone_num()}")
            new_phone = str(input('Enter new customer p[hone number]: '))
            customers_list[i].set_phone(new_phone)
        case _:
            print(f"Invalid choice!")
              

#Need function to validate input 


 
#Need dunction to verify if ID already existed 






