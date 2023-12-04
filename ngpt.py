import pandas as pd
import time
import numpy as np
import random


def calcVolume(mat):
    return np.sqrt(np.abs(np.linalg.det(mat @ mat.T)))

def maximize_volume(matrix, k):
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)

    # make approx matrix
    approx_matrix = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

    volume = calcVolume(approx_matrix)

    return volume

inp = pd.read_csv('input.csv')
matrix = inp.values


max_volume = 0
start_time = time.time()
current_volume = maximize_volume(matrix[:, :300], 20)

if current_volume > max_volume:
    max_volume = current_volume

end_time = time.time()

print(max_volume)
print(end_time-start_time)