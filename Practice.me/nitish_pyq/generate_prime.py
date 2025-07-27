def isPrime(n):
  if n<0 :  
    return False
  if n==2 :
    return True

  for i in range(2,n):
    if n%i==0:
        return False

  return True


l = int(input("Enter lower bound   "))
r = int(input("enter upper bound   "))

lst = []
for i in range (l,r+1):
    if isPrime(i):
        lst.append(i)

print(lst)       