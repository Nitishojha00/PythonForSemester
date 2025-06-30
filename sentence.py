sentence=input("enter a sentence:")

digit_count=0
uppercase_count=0
lowercase_count=0

for char in sentence:
 if char.isdigit():
  digit_count=digit_count+1
 elif char.isupper():
  uppercase_count=uppercase_count+1
 elif char.islower():
  lowercase_count=lowercase_count+1

print("Digits",digit_count)
print("uppercase letter",uppercase_count)
print("lower case letter",lowercase_count)