"""
Identity Matrix
An identity matrix is defined as a square matrix with 1s running from the top left of the square to the bottom right. The rest are 0s. The identity matrix has applications ranging from machine learning to the general theory of relativity.

Create a function that takes an integer n and returns the identity matrix of n x n dimensions. For this challenge, if the integer is negative, return the mirror image of the identity matrix of n x n dimensions.. It does not matter if the mirror image is left-right or top-bottom.

Examples
id_mtrx(2) ➞ [
  [1, 0],
  [0, 1]
]

id_mtrx(-2) ➞ [
  [0, 1],
  [1, 0]
]

id_mtrx(0) ➞ []
Notes
Incompatible types passed as n should return the string "Error".
"""

# Approach using numpy
def generate_identity_matrix(n):
    import numpy as np
    temp_n = abs(n)
    identity_matrix = np.zeros((temp_n,temp_n))
    for i in range(temp_n):
        identity_matrix[i][i] = 1
    if n>0:
        return identity_matrix
    else:
        return np.flip(identity_matrix, axis=0)
# print(generate_identity_matrix(-2))


# Approach without using numpy
def generate_identity_matrix_no_np(n):
    temp_n = abs(n)
    id_matrix = [[]]*temp_n
    
    for i in range(temp_n):
        id_matrix[i] = [0 for i in range(temp_n)]
        
    for i in range(temp_n):
        for j in range(temp_n):
            if i==j:
                id_matrix[i][j] = 1
                
    if abs(n)==n:
        return id_matrix
    else:
        id_matrix.reverse()
        return id_matrix

# print(generate_identity_matrix_no_np(2))
print(generate_identity_matrix_no_np(-2))