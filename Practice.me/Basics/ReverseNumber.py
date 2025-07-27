n = int(input("Enter a number   "))
val = 0
while n>0:
   r = n%10;
   n//=10;
   val = val*10+r;

print(val);