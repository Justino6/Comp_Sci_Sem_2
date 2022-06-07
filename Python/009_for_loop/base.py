x = int(input("Please enter a line length: "))
y = input("Do you want a horizontal or vertical line?: ")
if y == "horizontal":
    for x in range(0,x):
        print(" ", end="*")
elif y == "vertical":
    for y in range(0,x):
        print("*")