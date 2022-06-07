z = input("What symbol would you like to use?: ")
x = int(input("What width would you like your box to be?: "))
y = int(input("What height would you like your box to be?: "))
for i in range(0,y):
    print(" ")
    for j in range(0,x):
        print(" ", end = z)