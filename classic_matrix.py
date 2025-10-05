import random

def generate_random(n):
    matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(random.randint(-10, 10))
        matrix.append(row)
    return matrix


def classic(A, B):
    n = len(A)
    C = []

    for i in range(n):
        row = []
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += A[i][k] * B[k][j]
            row.append(sum)
        C.append(row)
    return C


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
    result = classic(A, B)

# OFFICIAL ALGORITHM RESULT
    print("Classic Matrix:")
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

    result = classic(test_1, test_2)

    print("Result: ")
    for row in result:
        print(row)