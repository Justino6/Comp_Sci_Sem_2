x = int(input("What is your first number?: "))
op = input("Enter your operation: ")
y = int(input("What is your second number?: "))
if op == "+":
    print(str(x)+op+str(y)+" = "+str(x+y))
elif op == "-":
    print(str(x)+op+str(y)+" = "+str(x-y))
elif op == "*":
    print(str(x)+op+str(y)+" = "+str(x*y))
elif op == "/":
    print(str(x)+op+str(y)+" = "+str(x/y))
else:
    print("uhhhhhh")