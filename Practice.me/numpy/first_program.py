import numpy as np

array = np.array([1,2,3])
# arr = np.append(array,3); // it dont make change in that array it will give new array arr have 1 2, 3, 3
#operation
print(np.mean(array))
print(np.sum(array))
print(array.size) # size
print("Slice:", array[0:2])

# create a 2d array matrix
matrix = np.array([[1,2,3],[2,3,4]])

#matrix operation
print("Matric:\n",matrix)
print("Transpose:\n",np.transpose(matrix))
print("Element wise addition:\n" ,matrix + 10)
print("Flattened:", array.flatten())