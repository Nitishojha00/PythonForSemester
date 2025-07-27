a = "  abc  "

print(a.strip())
print(len(a))
print(a[2:5])  # slicing
# print(isUpper(a[3]))


#  string concatenation ans string repetion
a = a.strip()
print(a*3)
print(a+"pPr")
print(a.capitalize())
print(a.upper())
print(a.lower())
a = a + " pqr"
print(a.title())
print(a[0].isupper())
print(a[0].lower())   # .lower()  convert to lower
print(a[1].islower())
b = "5"
print(b.isnumeric())
print("complete string is upper or not " , a.isupper())
print(b.isalnum()) # check string must all digit number or alphabet