def add(a , b):
    return a+b;

def subtract(a , b):
    return a-b;

def power(a,b):
    return a**b;

def multiply(a,b):
    return a*b;

n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))

print("Enter 1 for addition")
print("Enter 2 for subtraction")
print("Enter 3 for power")
print("Enter 4 for multiply")

choise  = int(input("Enter your choice"))
if choise == 1:
    print(add(n1,n2))
elif choise == 2:
    print(subtract(n1,n2))
elif choise == 3:
    print(power(n1,n2))
elif choise == 4:
    print(multiply(n1,n2))
else:
    print("Wrong Choise")
    

    