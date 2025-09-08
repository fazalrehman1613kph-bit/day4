inventory = {}
while True:
    print("\n1.Add a product")
    print("2.View a product")
    print("3.Remove a product")
    print("4.Exit")
    choice = input("What would you like to do?(1-4) ")
    if choice == "1":
            product_name = input("What would you like to add? ")
            price = int(input("What should be the price? "))
            inventory[product_name] = price
            print(f"Your inventory is {inventory}")
    elif choice == "2":
        for key,value in inventory.items():
            print(f"{key}: {value}")
    elif choice == "3":
        removed_item = input("What would you like to remove? ")
        if removed_item in inventory:
            del inventory[removed_item]
            print("Updated inventory is" , inventory)
        else:
            print("Invalid product")
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid number")