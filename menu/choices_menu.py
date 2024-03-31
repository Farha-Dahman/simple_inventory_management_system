from inventory.product import Product

def choices_menu(choice, inventory):
    # Dictionary mapping menu choices to corresponding functions
    options = {
        '1': add_product,
        '2': view_all_products,
        '3': edit_product,
        '4': delete_product,
        '5': search_product,
        '6': exit_program
    }

    # Check if the choice is valid or not
    if choice in options:
        return options[choice](inventory)
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
        return False

def add_product(inventory):
    # Function to add a new product to the inventory
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))
    product = Product(name, price, quantity)
    inventory.add_product(product)
    return False

def view_all_products(inventory):
    print("\n--- All Products ---")
    inventory.view_all_products()
    return False

def edit_product(inventory):
    # Function to edit the details of the product
    product_name = input("Enter product name to edit: ")
    new_name = input("Enter new name: ")
    new_price = float(input("Enter new price: "))
    new_quantity = int(input("Enter new quantity: "))
    inventory.edit_product(product_name, new_name, new_price, new_quantity)
    return False

def delete_product(inventory):
    # Function to delete a product from the inventory
    product_name = input("Enter product name to delete: ")
    inventory.delete_product(product_name)
    return False

def search_product(inventory):
    # Function to search for a product by its name
    name = input("Enter product name to search: ")
    inventory.search_product(name)
    return False

def exit_program(inventory):
    print("Exiting the program...")
    return True
