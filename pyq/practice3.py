with open("input.txt",'w') as f:
    f.write("12\n")
    f.write("13\n")
    f.write("14\n")
    f.write("15\n")
    f.write("16\n")
    f.write("17\n")
    f.write("18\n")

file=open("input.txt","rt")
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