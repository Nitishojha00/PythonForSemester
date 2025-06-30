with open("Input.txt",'w') as f:
  f.write("18\n")
  f.write("28\n")
  f.write("38\n")
  f.write("48\n")
  f.write("9\n")
  f.write("182\n")
  f.write("9\n")
  f.write("1\n")

file=open("Input.txt","rt")
for i in file:
 num=int(i)
 if(num%2==0):
   even=open("even.txt","a")
   even.write(str(num))
   even.write("\n")
 else:
   odd=open("odd.txt","a")
   odd.write(str(num))
   odd.write("\n")
