import random
import time

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
    
    sizes = [2, 4, 8, 16, 32, 64, 128, 256]

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

    print("Matrix A:")
    for row in A:
        print(row)
    
    print("\nMatrix B:")
    for row in B:
        print(row)

    print("\nClassic Matrix:")
    for row in result:
        print(row)


# TESTING ALGORITHM FOR REPORT ANALYSIS 
    print("\nTesting random matrix:")
    
    test_1 = generate_random(4)

    for n in sizes:
        A = generate_random(n)
        B = generate_random(n)
        start = time.perf_counter()  # high-resolution timer
        classic(A, B)
        end = time.perf_counter()
        print(f"Matrix size: {n}x{n}  |  Time: {end - start:.5f} sec")