
from classic_matrix import generate_random

def div_con_Matrix(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2

    A11, A12, A21, A22 = split4(A, mid)
    B11, B12, B21, B22 = split4(B, mid)

    P1 = div_con_Matrix(A11, B11)
    P2 = div_con_Matrix(A12, B21)
    P3 = div_con_Matrix(A11, B12)
    P4 = div_con_Matrix(A12, B22)
    P5 = div_con_Matrix(A21, B11)
    P6 = div_con_Matrix(A22, B21)
    P7 = div_con_Matrix(A21, B12)
    P8 = div_con_Matrix(A22, B22)

    C11 = add(P1, P2)
    C12 = add(P3, P4)
    C21 = add(P5, P6)
    C22 = add(P7, P8)

    # Reassemble the full matrix
    return join(C11, C12, C21, C22)

def add(X, Y):
    n = len(X)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(X[i][j] + Y[i][j])
        result.append(row)
    return result

def join(C11, C12, C21, C22):
    half = len(C11)
    combined = []

    # top half
    for i in range(half):
        combined.append(C11[i] + C12[i])

    # bottom half
    for i in range(half):
        combined.append(C21[i] + C22[i])

    return combined

def split4(M, mid):
    n = len(M)
    X11, X12, X21, X22 = [], [], [], []

    # top-left and top-right
    for i in range(mid):
        row11, row12 = [], []
        for j in range(mid):
            row11.append(M[i][j])
        for j in range(mid, n):
            row12.append(M[i][j])
        X11.append(row11)
        X12.append(row12)

    # bottom-left and bottom-right
    for i in range(mid, n):
        row21, row22 = [], []
        for j in range(mid):
            row21.append(M[i][j])
        for j in range(mid, n):
            row22.append(M[i][j])
        X21.append(row21)
        X22.append(row22)

    return X11, X12, X21, X22

if __name__ == "__main__":
    n = 4  # Size of the matrix (must be a power of 2 for simplicity)
    A = generate_random(n)
    B = generate_random(n)
    result = div_con_Matrix(A, B)

    print("Matrix A:")
    for row in A:
        print(row)
    
    print("\nMatrix B:")
    for row in B:
        print(row)

    print("\nDivide and Conquer Matrix:")
    for row in result:
        print(row)

    # TESTING ALGORITHM FOR REPORT ANALYSIS 
    print("\nTesting random matrix:")
    
    test_1 = generate_random(4)

    print("Matrix 1:")
    for row in test_1:
        print(row)

    test_2 = generate_random(4)
    print("Matrix 2:")

    for row in test_2:
        print(row)

    result = div_con_Matrix(test_1, test_2)

    print("Result: ")
    for row in result:
        print(row)