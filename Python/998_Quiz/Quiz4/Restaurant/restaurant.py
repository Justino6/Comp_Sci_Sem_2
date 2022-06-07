import random
restlist = ["Panda Express","Burger King","Taco Bell"]
pandamenu = ["Chow Mein","Orange Chicken","Beef and Broccoli"]
burgermenu = ["Cheeseburger","Fries","nuggets"]
tacomenu = ["Taco","Burrito","Soda"]
user = input("Pick a restaurant to eat at: " + restlist[0]+", "+ restlist[1]+", "+ restlist[2]+": ")
if user == "Panda Express":
    print(pandamenu)
    print(pandamenu[random.randrange(0,3)])
elif user == "Mcdonalds":
    print(burgermenu)
    print(burgermenu[random.randrange(0,3)])
elif user == "Taco bell":
    print(tacomenu)
    print(tacomenu[random.randrange(0,3)])