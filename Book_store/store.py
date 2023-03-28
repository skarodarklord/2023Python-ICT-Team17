class Store:
    def __init__(self, i, n, a, p):
        self.__id = i
        self.__name = n
        self.__address = a
        self.__phone = p
        
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone
        