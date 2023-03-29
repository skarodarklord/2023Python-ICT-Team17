class Customer:
    def __init__(self, id, name, dob, address, phone):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.__address = address
        self.__phone = phone
    
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