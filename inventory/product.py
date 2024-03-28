class Product:
    def __init__(self, name, price, quantity):
        # Initialize the product with name, price, and quantity
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price
    
    def set_quantity(self, quantity):
        self.__quantity = quantity   

    def display_product(self):
        print(f"Name: {self.__name}, Price: {self.__price}, Quantity: {self.__quantity}")

    def edit_product(self, new_name, new_price, new_quantity):
        # Method to edit the product details
        self.__name = new_name
        self.__price = new_price
        self.__quantity = new_quantity
