items_list = ["Bread" , "Milk" , "Eggs"]
print("Your order till now is: " , items_list)
choice = input("Would you like to add or remove anything?(a/r) ")
if choice == "a":
    added_item = input("What would you like to add? ")
    items_list.append(added_item)
    print("Now your order is:", ", ".join(items_list)) 

elif choice == "r":
    removed_item = input("What would you like to remove? ")
    if removed_item in items_list:
       items_list.remove(removed_item)
       print("Now your order is:", ", ".join(items_list)) 
    else:
        print("You have entered wrong item")
else:      
    print("You have entered invalid choice please select(a/r)")
    
for index, item in enumerate(items_list):
        print(f"Your order is #{index + 1}: {item}")
print()
  
prices = [10 , 20 , 30 , 40] 
total = 0
for price in prices:
    total = total + price
print(f"Your total is: ${total}")
print(f"Number of items: {len(prices)}")
print()
