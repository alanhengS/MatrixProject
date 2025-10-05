import random


def add_matrix(A, B):
    #Add two matrices A and B
    n = len(A)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result




def sub_matrix(A, B):
    #Subtract matrix B from A
    n = len(A)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(A[i][j] - B[i][j])
        result.append(row)
    return result




def strassen(A, B):
   #Strassen's matrix multiplication
    n = len(A)


   # Base case: 1x1 matrix
    if n == 1:
        return [[A[0][0] * B[0][0]]]


    mid = n // 2


   #spliting B into four sumbatrices


    A11, A12, A21, A22 = [], [], [], []


    for i in range(mid):
        # top left
        A11_row = []
        for j in range(mid):
            A11_row.append(A[i][j])
        A11.append(A11_row)


       # top right
        A12_row = []
        for j in range(mid, n):
            A12_row.append(A[i][j])
        A12.append(A12_row)


    for i in range(mid, n):
       # bottom left
        A21_row = []
        for j in range(mid):
            A21_row.append(A[i][j])
        A21.append(A21_row)


       # bottom right
        A22_row = []
        for j in range(mid, n):
            A22_row.append(A[i][j])
        A22.append(A22_row)


   #spliting B into four sumbatrices
    B11, B12, B21, B22 = [], [], [], []


    for i in range(mid):
        # top left
        B11_row = []
        for j in range(mid):
            B11_row.append(B[i][j])
        B11.append(B11_row)


       # top right
        B12_row = []
        for j in range(mid, n):
            B12_row.append(B[i][j])
        B12.append(B12_row)


    for i in range(mid, n):
        # bottom left
        B21_row = []
        for j in range(mid):
            B21_row.append(B[i][j])
        B21.append(B21_row)


       # bottom right
        B22_row = []
        for j in range(mid, n):
            B22_row.append(B[i][j])
        B22.append(B22_row)


  # the 7 products


    P1 = strassen(A11, sub_matrix(B12, B22))
    P2 = strassen(add_matrix(A11, A12), B22)
    P3 = strassen(add_matrix(A21, A22), B11)
    P4 = strassen(A22, sub_matrix(B21, B11))
    P5 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    P6 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))
    P7 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))




  #combining the results of the 7 products into quadrants


    temp1 = add_matrix(P5, P4)
    temp2 = sub_matrix(temp1, P2)
    C11 = add_matrix(temp2, P6)

    # Compute C12
    C12 = add_matrix(P1, P2)

    # Compute C21
    C21 = add_matrix(P3, P4)

    # Compute C22
    temp3 = add_matrix(P5, P1)
    temp4 = sub_matrix(temp3, P3)
    C22 = add_matrix(temp4, P7)




   #combining all the quadrants
    new_matrix = []


    for i in range(mid):
        new_matrix.append(C11[i] + C12[i])


    for i in range(mid):
        new_matrix.append(C21[i] + C22[i])


    return new_matrix




# to test the matrix
if __name__ == "__main__":
    A = [
        [2, 0, -1, 6],
        [3, 7, 8, 0],
        [-5, 1, 6, -2],
        [8, 0, 1, 7]
    ]


    B = [
        [0, 1, 6, 3],
        [-2, 8, 7, 1],
        [2, 0, -1, 0],
        [9, 1, 6, -2]
    ]


    result = strassen(A, B)


    print("Strassen's Matrix:")
    for row in result:
        print(row)  








