def circle():
    r = int(input("Enter the radius of the circle"))
    print(3.14*r*r);

def rectangle():
    l = int(input("Enter Length of the rectangle"))
    b = int(input("Enter Breadth of the rectangle"))
    print(l*b);
def square():
    a = int(input("Enter the length of the square"))
    print(a**2);


print(" Which shape area you want to print ");
print(" click 1 for circle ")
print(" click 2 for rectangle ")
print(" click 3 for square ")

n = int(input("Enter choise"))


if n==1:
   ans =  circle()
elif n==2:
    ans = rectangle()
else:
    ans = square()

