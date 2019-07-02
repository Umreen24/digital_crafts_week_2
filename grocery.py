
from shopping_class import ShoppingList
from grocery_item_class import GroceryItem

user_input = ""
shopping_lists = []

while user_input != "q":

    if user_input == "1":
        title = input("Enter grocery store: ")
        address = input("Enter street name of grocery store: ")

        shopping_list = ShoppingList(title, address)
        shopping_lists.append(shopping_list)

    elif user_input == "2":

        for index in range(0,len(shopping_lists)):
            print(f"{index +1} - {shopping_lists[index].title} - {shopping_lists[index].address}")

    elif user_input == "3":

        shopping_list_number = int(input("Enter the store number to add items to: "))
        title = input("Enter grocery item: ")
        price = input("Enter price for grocery item: ")
        quantity = input("Enter quantity of grocery item needed: ")

        shopping_list_to_add_items = shopping_lists[shopping_list_number - 1]

        grocery_item = GroceryItem(title,price,quantity)

        shopping_list_to_add_items.grocery_items.append(grocery_item)
    
    elif user_input == "4": 

        for x in range(0, len(shopping_lists)):
            print('\n')
            print(f"{shopping_lists[x].title} - {shopping_lists[x].address}")
            for y in range(0, len(shopping_lists[x].grocery_items)):
                print(f" Item: {shopping_lists[x].grocery_items[y].title} - Quantity: {shopping_lists[x].grocery_items[y].quantity} ")
                
    user_input = input("Press 1 to enter a store, press 2 to view stores, press 3 to add an item to a store, press 4 to view your stores and items, press q to quit! ")