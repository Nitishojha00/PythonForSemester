string=input("enter a string:")
count_vowel=0
count_consonant=0
 
vowel=("aeiouAEIOU")
for alphabet in string:
  if alphabet in vowel:
    count_vowel=count_vowel+1
  else:
    count_consonant=count_consonant+1

print("vowels are:",count_vowel)
print("consonants are:",count_consonant)
 