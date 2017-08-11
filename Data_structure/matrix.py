# Need to implement the matrix class
# Left Strassen's algorithm to implement

def square_matrix_multiply(A, B):
    assert len(A) == len(B), 'differt size of matrix'
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


def square_matrix_multiply_recursive(A, B):
    assert len(A) == len(B), 'differt size of matrix'
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]

    if n == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        A_11, A_12, A_21, A_22 = __partition_matrix(A)
        B_11, B_12, B_21, B_22 = __partition_matrix(B)
        C_11, C_12, C_21, C_22 = __partition_matrix(C)

        C_11 = square_matrix_multiply_recursive(A_11, B_11) + square_matrix_multiply_recursive(A_12, B_21)
        C_12 = square_matrix_multiply_recursive(A_11, B_12) + square_matrix_multiply_recursive(A_12, B_22)
        C_21 = square_matrix_multiply_recursive(A_21, B_11) + square_matrix_multiply_recursive(A_22, B_21)
        C_22 = square_matrix_multiply_recursive(A_21, B_12) + square_matrix_multiply_recursive(A_22, B_22)


def __partition_matrix(matrix):
    n = len(matrix)

    top_martix = matrix[:n // 2]
    top_left = [row[:n // 2] for row in top_martix]
    top_right = [row[n // 2:] for row in top_martix]

    bottom_matrix = matrix[n // 2:]
    bottom_left = [row[:n // 2] for row in bottom_matrix]
    bottom_right = [row[n // 2:] for row in bottom_matrix]

    return top_left, top_right, bottom_left, bottom_right
