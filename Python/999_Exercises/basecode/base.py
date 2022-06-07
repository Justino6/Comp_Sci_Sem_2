numitems = int(input("How many items do you want to buy?: "))
total = 0
for i in range(0,numitems):
    item = str(input("What item are you buying?: "))
    cost = float(input("How much does the item cost?: "))
    print("Thanks for buying "+item)
    print("______________________________________________________________________________")
    total = total+cost
    print("Your total is: "+str(total))