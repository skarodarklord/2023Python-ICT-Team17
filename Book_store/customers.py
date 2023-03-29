class Customer:
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