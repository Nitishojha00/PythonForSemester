s = "ABC.EFG.HIJ.KLM.ABC"
print(s.split('.'))
# sorting sring 
print(sorted(s))

#  remove dot using replace 
print(s.replace('.', ''))


print(s.count("ABC"))

#  Reverse String
print(s[::-1])


# count alphabet 
cnt = 0
for i in range(0,len(s)):
    if s[i] in ['a','e','i','o','u','A','E','I','O','U']:
     cnt+=1
print(cnt)



