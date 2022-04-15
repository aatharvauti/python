import numpy as np

# Creating array object
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )

print("\nType of array: ", type(arr))

print("\nNo. of dimensions: ", arr.ndim)

print("\nShape of array: ", arr.shape)

print("\nSize of array: ", arr.size)

print("\nType of elements stored in array: ", arr.dtype)

arr1 = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

newarr = arr1.reshape(2, 2, 3)

print ("\nOriginal array:\n", arr)
print ("\nReshaped array:\n", newarr)

b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)

c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)

d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s." 
            "Array type is complex:\n", d)

e = np.random.random((2, 2))
print ("\nA random array:\n", e)

f = np.arange(0, 30, 5)
print ("\nA sequential array with steps of 5:\n", f)

temp = arr1[:2, ::2]
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp)

temp = arr1[[0, 1, 2], [2, 1, 0]]
print ("\nElements at indices (0, 2), (1, 1), (2, 0)\n", temp)

cond = arr1 > 0 
temp = arr1[cond]
print ("\nElements greater than 0:\n", temp)

print ("\nAdding 1 to every element:", arr1+1)

print ("\nSubtracting 3 from each element:", arr1-3)

print ("\nMultiplying each element by 10:", arr1*10)

print ("\nSquaring each element:", arr1**2)

arr1 *= 2
print ("\nDoubled each element of original array:", arr1)

print ("\nOriginal array:\n", arr1)
print ("\nTranspose of array:\n", arr1.T)

print ("\nArray sum:\n", arr1 + arr1)

print ("\nArray multiplication:\n", arr1*arr1)

print ("\nLargest element is:", arr1.max())

print ("\nRow-wise maximum elements:",
                    arr1.max(axis = 1))

print ("\nColumn-wise minimum elements:",
                        arr1.min(axis = 0))

print ("\nSum of all array elements:",
                            arr1.sum())

print ("\nCumulative sum along each row:\n",
                        arr1.cumsum(axis = 1))
