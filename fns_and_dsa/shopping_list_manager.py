def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    while True:
        display_menu()

        # Validate user input for menu choice
        choice = input("Enter your choice: ")

        # Check if the input is a valid number
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        choice = int(choice)  # Convert the choice to an integer

        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item name to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")

        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Your shopping list:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
