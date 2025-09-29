# Systems of Linear Equations & Model Fitting


#*Gaussian Elimination from Scratch

A = [
    [0, 1, 3],
    [4, 4, 7],
    [2, 5, 0]
]

b = [1, 1, 3]

#making augmented matrix
A = [row + [b[i]] for i, row in enumerate(A)]
print("Augmented matrix:",A)

def forward_elimination(A):
    for i in range(len(A)):
        pivot = A[i][i]  #i-th row and i-th column = diagonal element
        if pivot == 0:
            for m in range(i+1, len(A)):
                if A[m][i] != 0:  #The element in the i-th column should be non-zero
                    A[i], A[m] = A[m], A[i]  #Swap the rows
                    pivot = A[i][i]
                    break
        pivot=A[i][i]  #new pivot
        A[i]=[r/pivot for r in A[i] ] #making pivot 1
        for c in range(i+1,len(A)):
            A[c] = [A[c][j] - A[c][i] * A[i][j] for j in range(len(A[i]))] #Using the pivot row to make the elements below the pivot zero"
                        
            
    return A



def back_substitution(A):
    n = len(A) #Number of the rows
    m = len(A[0]) - 1   #Number of variables-columns(excluding the last column)
    x = [0 for _ in range(m)]  #Create x with default values of 0

    #Checking the solutions of the system
    for row in A:
        only_zeros = 1
        for c in row[:-1]:
            if c != 0:
                only_zeros = 0
                break
        if only_zeros == 1 and row[-1] != 0:
        
                return "No Solution!"

    pivot_count = 0
    for i in range(n):
        pivot_found = 0
        for j in range(m):
            if A[i][j] != 0:
                pivot_found = 1
                break
        pivot_count += pivot_found

    if pivot_count < m:
        return "Infinity Solutions!"

    for i in range(n - 1, -1, -1):
        right = A[i][-1]
        for j in range(i + 1, m):
            right -= A[i][j] * x[j]
        x[i] = right / A[i][i]

    return x, len(x)


augmented = forward_elimination(A)
print("Upper triangular matrix:", augmented)

result = back_substitution(augmented)
print("Solution (from scratch):", result)


import numpy as np

A2 = [
    [0, 1, 3],
    [4, 4, 7],
    [2, 5, 0]
]
b2 = [1, 1, 3]

np_A = np.array(A2, dtype=float)
np_b = np.array(b2, dtype=float)

np_solution = np.linalg.solve(np_A, np_b)
print("Solution (NumPy):", np_solution)

