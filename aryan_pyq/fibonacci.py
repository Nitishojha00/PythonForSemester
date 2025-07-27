number=int(input("enter the value of x:"))
x1=0
x2=1
count=2
if(number<0):
    print("please enter a positive integer")
elif (number==1):
    print("fibonacci series is")
    print(x1)
else:
    print("Fibonacci series is :")
    print(x1,",",x2,end=", ")
    while(count<number):
        xth=x1+x2
        print(xth,end=", ")

        x1=x2
        x2=xth
        count+=1


#m2
def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    

terms=int(input("enter the number of terms:"))
print("fibonacci series:")

for i in range (terms):
 print(fib(i),end=",")
    

