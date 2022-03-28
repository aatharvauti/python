# Python3 program to multiply two matrices.
MAX = 100

# Function to print Matrix
def print_matrix(M, rowSize, colSize) :
	
	for i in range(rowSize) :
		for j in range(colSize) :
			print(M[i][j], end = " ")

		print()

# Function to multiply two matrices
# A[][] and B[][]
def multiply_matrix(row1, col1, A,
				row2, col2, B) :
						
	# Matrix to store the result
	C = [[0 for i in range(MAX)]
			for j in range(MAX)]

	# Check if multiplication is Possible
	if (row2 != col1) :
		print("Not Possible")
		return
	
	# Multiply the two
	for i in range(row1) :
		for j in range(col2) :
			C[i][j] = 0
			for k in range(row2) :
				C[i][j] += A[i][k] * B[k][j];

	# Print the result
	print("Resultant Matrix: ")
	print_matrix(C, row1, col2)

# Driver Code
if __name__ == "__main__" :

	A = [[0 for i in range(MAX)]
			for j in range(MAX)]
	B = [[0 for i in range(MAX)]
			for j in range(MAX)]

	# Read size of Matrix A from user
	row1 = int(input("Enter the number of rows for the first matrix: "))
	col1 = int(input("Enter the number of columns for the first matrix: "))

	# Read the elements of Matrix A from user
	print("Enter the elements of First matrix: ");
	for i in range(row1) :
		for j in range(col1) :
			A[i][j] = int(input("A[" + str(i) +
								"][" + str(j) + "]: "))

	# Read size of Matrix B from user
	row2 = int(input("Enter the number of rows for the second matrix: "))
	col2 = int(input("Enter the number of columns for the second matrix: "))

	# Read the elements of Matrix B from user
	print("Enter the elements for the second matrix: ");
	for i in range(row2) :
		for j in range(col2) :
			B[i][j] = int(input("B[" + str(i) +
								"][" + str(j) + "]: "))

	# Print the Matrix A
	print("First Matrix: ")
	print_matrix(A, row1, col1)

	# Print the Matrix B
	print("Second Matrix: ")
	print_matrix(B, row2, col2)

	# Find the product of the 2 matrices
	multiply_matrix(row1, col1, A, row2, col2, B)

