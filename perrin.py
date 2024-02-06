import numpy as np
from numpy.linalg import matrix_power

def perrin(n):
    base_matrix = np.array([[0, 1, 1], [1, 0, 0], [0, 1, 0]])
    initial_vector = np.array([2, 0, 3])

    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2

    multiplied_matrix = matrix_power(base_matrix, n - 2)
    return np.matmul(multiplied_matrix, initial_vector)[0]