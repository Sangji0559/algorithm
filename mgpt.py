import numpy as np
import pandas as pd
import random
import time

def calcVolume(mat):
    return np.sqrt(np.abs(np.linalg.det(np.dot(mat.T, mat))))

def sortMatrixByVolume(matrix):
    volumes = [calcVolume(matrix[:, i:i+1]) for i in range(matrix.shape[1])]
    sorted_indices = np.argsort(volumes)[::-1]
    sorted_matrix = matrix[:, sorted_indices]
    return sorted_indices

def findMaxVolume(init, matrix):
    includeIndex = [init]
    max_matrix = matrix[:, init:init+1]
    for k in range(19):
        max_volume = 0
        maxIndex = 0
        for i in range(matrix.shape[1]):
            subset = max_matrix[:]
            if i in includeIndex:
                continue

            #subset = np.hstack((max_matrix, matrix[:, i:i+1]))
            subset = np.hstack((matrix[:, i:i+1], max_matrix))

            volume = calcVolume(subset)
            if max_volume < volume:
                max_volume = volume
                max_subset = matrix[:, i:i+1]
                maxIndex = i

        #max_matrix = np.hstack((max_matrix, max_subset))
        max_matrix = np.hstack((max_subset, max_matrix))

        includeIndex.append(maxIndex)

    print(max_matrix)

    return max_matrix, includeIndex

idx = 25

inp = pd.read_csv('input.csv')
matrix = inp.values

init_index = sortMatrixByVolume(matrix)

start = time.time()
best_matrix, best_index = findMaxVolume(init_index[idx], matrix)
best_volume = calcVolume(best_matrix)
end = time.time()
sec = end - start
print(best_index)
print(best_volume)
print(f"{sec}m/s")