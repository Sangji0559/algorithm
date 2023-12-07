import numpy as np
import pandas as pd
import random
import time

def calcVolume(mat):
    return np.sqrt(np.abs(np.linalg.det(np.dot(mat.T, mat))))

def findMaxVolume():
    includeIndex = []
    max_matrix = []
    for k in range(20):
        max_subset = []
        max_volume = 0
        maxIndex = 0
        for i in range(matrix.shape[1]):
            subset = max_matrix[:]
            if i in includeIndex:
                continue
            if k == 0:
                subset = matrix[:, i:i+1]
            else:
                subset = np.hstack((matrix[:, i:i+1], max_matrix))

            volume = calcVolume(subset)
            if max_volume < volume:
                max_volume = volume
                max_subset = matrix[:, i:i+1]
                maxIndex = i
        if k == 0:
            max_matrix = max_subset
        else:
            max_matrix = np.hstack((max_subset, max_matrix))

        includeIndex.append(maxIndex)

    return max_matrix, includeIndex

inp = pd.read_csv('input.csv')
matrix = inp.values

start = time.time()
best_matrix, best_index = findMaxVolume()
best_volume = calcVolume(best_matrix)
end = time.time()
sec = end - start
print(best_index)
print(best_volume)
print(f"{sec}m/s")