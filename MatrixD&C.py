def div_con_Mat(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2

    A11, A12, A21, A22 = split4(A, mid)
    B11, B12, B21, B22 = split4(B, mid)

    P1 = div_con_Mat(A11, B11)
    P2 = div_con_Mat(A12, B21)
    P3 = div_con_Mat(A11, B12)
    P4 = div_con_Mat(A12, B22)
    P5 = div_con_Mat(A21, B11)
    P6 = div_con_Mat(A22, B21)
    P7 = div_con_Mat(A21, B12)
    P8 = div_con_Mat(A22, B22)

    # C11 = (P1 + P2)
    # C12 = (P3 + P4)
    # C21 = (P5 + P6)  
    # C22 = (P7 + P8)


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
