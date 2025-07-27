with open("n.txt","w") as n:
   n.write("2\n")
   n.write("3")

with open("n.txt","r") as n ,open("e.txt","w") as e , open("o.txt","w") as o:

   values = n.readlines()
   for val in values:
      num = int(val.strip());
      if num%2==0:
        e.write(str(num))
        e.write("\n")
      else:
        o.write(str(num))
        o.write("\n")

with open ("e.txt","r") as e:
     print(e.readlines())

with open ("o.txt","r") as o:
     print(o.readlines())
   