def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if(b==0):
        print("division not possible by 0")
        return None
    else:
        return a/b
    
print("select Operations:")
print("1:add")
print("2:subtract")
print("3:multiply")
print("4:divide")

num1=int(input("enter 1 number:"))
num2=int(input("enter 2 number:"))

choice=input("enter choice(1/2/3/4):")

if choice=='1':
    print(num1 ,"+", num2,"=",add(num1,num2))
elif choice=='2':
    print(num1 ,"-", num2,"=",subtract(num1,num2))
elif choice=='3':
    print(num1 ,"*", num2,"=",multiply(num1,num2))
elif choice=='4':
    print(num1 ,"/", num2,"=",divide(num1,num2))
else:
    print("invalid operation")