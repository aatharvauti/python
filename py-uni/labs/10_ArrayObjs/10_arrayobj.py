import numpy as np

list1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"List 1:\n{list1}")

list2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(f"List 2:\n{list2}")

list3 =  np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"List 3:\n{list3}")

# Dimension
print("\nDimension of arrays:\n")
print(list1.ndim)
print(list2.ndim)
print(list3.ndim)

# Shape
print("\nShape of the arrays:\n")
print(list1.shape)
print(list2.shape)
print(list3.shape)

# Datatype
print("\nDatatype of the arrays:\n")
print(list1.dtype)
print(list2.dtype)
print(list3.dtype)

# Number of Elements
print("\nNumber of Elements:\n")
print(list1.size)
print(list2.size)
print(list3.size)

# Items Size
print("\nItem Size:\n")
print(list1.itemsize)
print(list2.itemsize)
print(list3.itemsize)

# Parse elements
print("\nElement in the first row and third column:\n")
print(list2[1, 3])

# Parse rows and columns
print(list2[0, :])
print(list2[:, 0:3])
print(list2[:, 1])

# 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:\n")
print(arr3d)

# Parse elements
print("\nElement in the first row and third column:\n")
print(arr3d[1, 0, 1])

# range
print(arr3d[:, 1, :])

# replace
arr3d[:, 1, :] = [[9, 9],[8, 8]]
print(arr3d)

# copping array
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print(b)
print(a)

# Mathematics
print ("Adding 1 to every element:", list2+1)
print ("Subtracting 3 from each element:", list2-3)
print ("Multiplying each element by 10:", list2*10)
print ("Squaring each element:", list2**2)

list2 *= 2
print ("Doubled each element of original array:", list2)