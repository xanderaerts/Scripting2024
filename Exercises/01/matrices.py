# %% [markdown]
# # Matrices 
# 
# In this assignment, you will work with nested lists to represent matrices. Create a script called matrices.py. IMPORTANT: You're not allowed to use any libraries in this assignment.
# 
# In this script, you will load in a matrix and create functions to do a scalar multiplication and transpose operation with a matrix. Both functions require you to create a new nest matrix and fill that with the processed elements of the given matrix. You can use the list .append() function to append respectively elements and full rows to a list / matrix.
# 
# In matrices.py create these three functions:
# 
# - read_matrix(): Ask the user to input a matrix per row, with spaces between the numbers / items of the matrix. You do not need input checking (i.e. check if the input is a digit or if all rows are equal     length) as we expect the user to input a valid matrix. Make sure to cast all input to integers. Return the matrix once the user inputs nothing.
#     
# - scalar_multiplication(matrix, scalar): In a scalar multiplication, you will multiply each individual component in the matrix with the given scalar. This function should return the resulting matrix.
# 
# - transpose(matrix): A transpose of a matrix is an operation that flips the matrix over its diagonal, in other words: it switches the rows and columns. This function should return the transposed matrix (please note that the size of the transposed matrix is often different from the original).
# - 
# Example usage:
# ``` 
# $ python3 matrices.py
# Please input your matrix below:
# 3 2 1
# 1 2 3
# Your matrix:
# [[3, 2, 1], [1, 2, 3]]
# Scalar multiplication with 8:
# [[24, 16, 8], [8, 16, 24]]
# Transposition:
# [[3, 1], [2, 2], [1, 3]]
# 
# $ python3 matrices.py
# Please input your matrix below:
# 1 2
# 3 4
# 5 6
# 7 8
# Your matrix:
# [[1, 2], [3, 4], [5, 6], [7, 8]]
# Scalar multiplication with 8:
# [[8, 16], [24, 32], [40, 48], [56, 64]]
# Transposition:
# [[1, 3, 5, 7], [2, 4, 6, 8]] 
# ```

# %%
def read_matrix():
    print("Please input your matrix below")

    matrix = []
    raw = input()

    while raw != "":
        matrix.append([int(i) for i in raw.split()])
        raw = input()
    return matrix

# %%
def scalar_multiplication(matrix, scalar): 
    multipyMatrix = []

    for row in matrix:
        newRow = []
        for col in row:
            newRow.append(col* scalar)
        multipyMatrix.append(newRow)

    return multipyMatrix 

# %%
def transpose(matrix):
    transMaxtrix = []

    for i in range(len(matrix[0])):
        newrow = []
        for j in range( len(matrix)):
            newrow.append(matrix[j][i])
        transMaxtrix.append(newrow)
    return transMaxtrix 

# %% [markdown]
# ## Main Code

# %%
if __name__ == "__main__":
    matrix = read_matrix()
    print("Your matrix:")
    print(matrix)

    scalar = 8

    newmatrix = scalar_multiplication(matrix, scalar)
    print("Scalar multiplication with 8:")
    print(newmatrix)

    transMatrix = transpose(matrix)
    print("Transposition:")
    print(transMatrix)


