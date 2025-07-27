#  okay Basic to advance

list = []       #initialization

list.append(2)
list.append("abc")
list.extend([2,3,4]) 

print(list)

list1 = [1,2,3,4,-1]

print([x for x in list1 if x<0])