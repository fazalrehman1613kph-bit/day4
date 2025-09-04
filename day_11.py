items_list = ["Breads" , "Milk" , "Eggs"]
print("Your order till now is :" , items_list)
choice = input("Would you like to add or remove anything?(a/r)") 
if choice == "a":
    added_item = input("Please enter your desired product: ")
    items_list.append(added_item)
    print("Now your order is: ", "," .join(items_list))
elif choice == "r":
    removed_item = input("What would you like to remove?: ")
    if removed_item in items_list:
        items_list.remove(removed_item)
        print("Now your order is: " , "," .join(items_list))
    else:
            print(f"Sorry, {removed_item} is not in the list")
else:
    ("You have entered an invalid choice.")            