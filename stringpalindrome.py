string=input("enter a string:")

rev_string=string[::-1]
print(rev_string)
if string==rev_string:

    print(string,"is palindrome")
else:
    print(string,"is not palindrome")