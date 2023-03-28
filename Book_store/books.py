#ID
#Title
#Genre
#Author
#Year of publication
#Target audience: Children(3-16)😭, Young adults(17-30), Middle-aged adults(31-45), Old adults(>45)
#(Date of importation)
#(Import) quantity
#Price

class Book:
    def __init__(self, i, t, g, a, y):
        self.__id = i
        self.__title = t
        self.__genre = g
        self.__author = a
        self.__pub_year = y
        self.__target_audience = None
        self.__price = 0
        
    def get_id(self):
        return self.__id
    
    def get_title(self):
        return self.__title
    
    def get_genre(self):
        return self.__genre
    
    def get_author(self):
        return self.__author
    
    def get_pub_year(self):
        return self.__pub_year
    
    def set_target(self):
        print(f"Choose the target audience of this book:\n"
              f"1. Children (3-16) \n"
              f"2. Young adults (17-30) \n"
              f"3. Middle-aged adults (30-45) \n"
              f"4. Old adults (Above 45) \n")
        op = int(input(f"Your choice: "))
        match op:
            case 1:
                self.__target_audience = "Children"
            case 2:
                self.__target_audience = "Young adults"
            case 3:
                self.__target_audience = "Middle-aged adults"
            case 4:
                self.__target_audience = "Old adults"
            case _:
                print(f"Invalid choice!")
                
    def get_target(self):
        return self.__target_audience
    
    def set_price(self):
        price = int(input("Enter price (VND): "))
        self.__price = price
        
    def get_price(self):
        return self.__price
            
        
    
    