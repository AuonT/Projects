status = "stay"
name = input("hello what is your name? ")
print()
money = float(input("how much money do you have? "))
print()
if money <= 2.75:
    print("sorry, you don't have enough money to order anything.")    
    while money <=2.75:

        print()
        moneyretry = input("more money yet? (y/n) ")
        print()
        if moneyretry == "y":
            money = float(input("how much money do you have? "))
            print()
        else: 
            print("sorry")
else:
    while status == "stay":
        burgers = int(input("how many burgers would you like to order? "))
        print()
        fries = int(input("how about fries? "))

        burgercost = 5.50
        frycost = 2.75
        total = (burgers * burgercost) + (fries * frycost)
        if money >= total:
            print(f"thank you for ordering {name}! your total is ${total:.2f}.")
            print()
            print(f"you have ${money - total:.2f} left over.")
            exit()
        elif money < total:
            status = input("sorry, you don't have enough money to complete this order.\nPlease try again by typing 'stay'.\nIf not type 'exit'")
            if status != "stay" and status != "exit":
                print("please try typing either 'stay' or 'exit'")
        elif status == "exit":
            exit()
        else:
            print("please try again.")
        