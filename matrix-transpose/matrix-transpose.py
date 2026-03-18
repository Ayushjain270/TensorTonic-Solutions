import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    rows = len(A)
    cols = len(A[0])

    transpose = []
    for j in range(cols):
        new_list = []
        for i in range(rows):
            new_list.append(A[i][j])
        transpose.append(new_list)

    
    return np.array(transpose)
    
