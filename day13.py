items_list = ["Bread", "Milk", "Eggs"]
print("Your order till now is:", items_list)

# Start a loop that runs until the user chooses to exit
while True:
    # Ask for the user's choice each time
    choice = input("\nWould you like to add or remove anything? (a/r/x to exit): ").strip().lower()
    
    if choice == "a":
        added_item = input("What would you like to add? ").strip()
        items_list.append(added_item)
        print("Now your order is:", ", ".join(items_list))
    elif choice == "r":
        removed_item = input("What would you like to remove? ").strip()
        if removed_item in items_list:
            items_list.remove(removed_item)
            print("Now your order is:", ", ".join(items_list))
        else:
            print(f"Sorry, '{removed_item}' is not in the list.")
    elif choice == "x":  # 'x' for exit
        print("Goodbye!")
        break  # Exit the loop
    else:
        print("Invalid choice. Please enter 'a', 'r', or 'x' to exit.")