
def isPrime(n):
    ans = True
    if n==2:
     ans = True
    if n==1:
     ans = False
    else:
        for i in range (2,n//2+1):
            if n%i==0:
                ans = False
                break

    if ans:
        return True
    else:
        return False


n = int(input("Enter a Number to Check Prime"))
for i in range (1,n+1):
    ans = isPrime(i)
    if ans:
     print(i , " is Prime" )
    else:
     print(i , " is Not Prime")