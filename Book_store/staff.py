# Staff ID: str
# Staff name: str
# DoB: str
# Address: str
# Phone number: str
# Salary
# (Staff level)

#Can: Modify books info, input books, see books & store info, see & modify customers list

class Staff:
    def __init__(self, i, n, d, a, p):
        self.__id = i
        self.__name = n
        self.__dob = d
        self.__address = a
        self.__phone = p
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob
    
    def get_addr(self):
        return self.__address
    
    def get_phone_num(self):
        return self.__phone
    
    #For admins
    def set_salary(self, s):
        self.__salary = s
        
    def get_salary(self):
        return self.__salary    
    
    #Only staff & admin available, don't need this
    #def set_level(self):
    #    print(f"Choose staff level: \n
    #          1. ")
        