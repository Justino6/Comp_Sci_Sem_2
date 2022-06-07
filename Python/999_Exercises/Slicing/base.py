first = input("Please enter a first name: ")
last = input("Please enter a last name: ")
num1 = -1
num2 = 0
for i in range(len(first)):
    num1 = num1 + 1
    num2 = num2 + 1
    print(first[num1:num2])
    
print(" ")
num3 = -1
num4 = 0
for j in range(len(last)):
    num3 = num3 + 1
    num4 = num4 + 1
    print(last[num3:num4])