from inventory.inventory import Inventory
from menu.display_menu import display_menu
from menu.choices_menu import choices_menu

def main():
    inventory = Inventory()

    while True:
        # Display the menu options to the user
        display_menu()
        choice = input("Enter your choice: ")
        
        # Call the choices_menu function to handle the user's choice
        # If the function returns True, break out of the loop and exit the program
        if choices_menu(choice, inventory):
            break

if __name__ == "__main__":
    main()