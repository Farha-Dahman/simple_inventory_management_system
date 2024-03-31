from typing import List
from inventory.product import Product

class Inventory:
    def __init__(self):
        # Initialize private attribute to store products
        self.__products: List[Product] = []

    def get_products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def view_all_products(self):
        for product in self.__products:
            product.display_product()

    def edit_product(self, product_name, new_name, new_price, new_quantity):
        # Method to edit the details of the product
        for product in self.__products:
            if product.get_name() == product_name:
                product.edit_product(new_name, new_price, new_quantity)
                print("Product edited successfully.")
                return
        print("Product not found.")

    def delete_product(self, product_name):
        # Method to delete a product from the inventory
        for product in self.__products:
            if product.get_name() == product_name:
                self.__products.remove(product)
                print("Product deleted successfully.")
                return
        print("Product not found.")

    def search_product(self, product_name):
        # Method to search for a product by its name
        for product in self.__products:
            if product.get_name() == product_name:
                print("Product found:")
                product.display_product()
                return
        print("Product not found.")
