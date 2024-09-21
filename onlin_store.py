from colorama import Fore, Back, Style, init
init(autoreset=True)


#dICKCHINERY of the avalible itemes
avilable_itemes = {
    "iphone 15 ":{
        "price": 1500,
        "quantity": 15
    },
     "iphone 15 pro ":{
        "price": 1700,
        "quantity": 20
    },
      "iphone 15 pro max ":{
        "price": 2000,
        "quantity": 1
    }
}
basket= {}
#make loop until the user quit the program
while True:
    #print user choises screen
    user_message = ''' what you would like to do?
    1.view the avilable items
    2.view the basket card
    3.view total price of the basket
    4.quit'''
    print(user_message)
    #get the user choise
    user_choice = input(Fore.YELLOW + "Enter number of what you want to do: " + Style.RESET_ALL)
#if user want to see the avilable items and buy
    if user_choice == "1":
        print(Back.MAGENTA + Fore.WHITE + "The available items are:" + Style.RESET_ALL)
        for i , item in enumerate(avilable_itemes,1):
            item_price = avilable_itemes[item]["price"]
            item_quantity = avilable_itemes[item]["quantity"]
            if item_quantity == 0:
              print(f"{i}. {item}: {item_price}$ {Fore.RED} (not available){Style.RESET_ALL}")
            else:
                print(f"{i}.{item}: {item_price}$ ")
 #get the item that user want it
        number_item = int(input(Fore.CYAN + "Enter the number of the items to buy it (Enter '0' to return to menu): " + Style.RESET_ALL))
        if number_item == 0:
            continue
        item_name = list(avilable_itemes.keys())[number_item -1]
        #check if the item avilable
        avilable_quantity = avilable_itemes[item_name]["quantity"]
        if avilable_quantity == 0:
            print("Sory,The item is not avilable")
            
            continue
        avilable_itemes[item_name]["quantity"]-=1
    #Add the selcted item to the baskit and update the quantity if user selecet same item again
        order_price = avilable_itemes[item_name]["price"]
        if item_name not in basket:
            order_quantity =1
        else:
            order_quantity+=1
            
        order_info = {
            item_name:{
                "price":order_price,
                "quantity": order_quantity
            }
        }
        basket.update(order_info)
        
        print(Fore.GREEN + f"{item_name} added to the basket" + Style.RESET_ALL)
    # #if user want to see the basket
    elif user_choice == "2":
        if basket:
            print(Back.CYAN + Fore.BLACK + "Your Basket:" + Style.RESET_ALL)
            for item  in basket:
                price= basket[item]["price"]
                quantity= basket[item]["quantity"]
                print(f"{Fore.GREEN}{item}: {price}$ * {quantity} = {price * quantity}${Style.RESET_ALL}")
        else:
            print(Fore.RED + "The basket is empty" + Style.RESET_ALL)
    elif user_choice == "3":
        list_total = [basket[item]["price"] * basket[item]["quantity"] for item  in basket]
        sum_total = sum(list_total)
        print(Fore.GREEN + f"The total price is {sum_total}$" + Style.RESET_ALL)
    elif user_choice == "4":
        print(Fore.RED + "Ending the program..." + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Enter a valid number between 1 and 4" + Style.RESET_ALL)
        continue
        
    
       