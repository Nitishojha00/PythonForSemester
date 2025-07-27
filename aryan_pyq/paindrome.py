num=int(input("enter a number:"))
rev=0
original=num 
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

if(rev==original):
        print("given number is palindrome")
else:
        print("not palindome")




