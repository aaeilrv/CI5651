import numpy as np

A = [2, 2, 1, 22, 15]

def good_subarrays(A):

    matrix = np.zeros((len(A), len(A)))
    
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if j >= i:
                if A[j] % (i+1) == 0:
                    if i == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = sum(matrix[i-1][0:j])  

    return int(np.sum(matrix))

if __name__ == "__main__":
    print(good_subarrays(A))