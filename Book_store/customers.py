class Customer:
    def __init__(self, id, name, dob, address, phone):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__address = address
        self.__phone = phone
    
    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id
    
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_dob(self, dob):
        self.__dob = dob
    
    def get_dob(self):
        return self.__dob
    
    def set_addr(self, addr):
        self.__address = addr

    def get_addr(self):
        return self.__address
    
    def set_phone(self, phone):
        self.__phone = phone
    
    def get_phone_num(self):
        return self.__phone
    
#Perhaps should remove addr, we do not do shipping btw