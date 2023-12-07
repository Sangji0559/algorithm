import pandas as pd
import numpy as np
import time

def calculate_volume(matrix):
    return np.sqrt(abs(np.linalg.det(matrix.T @ matrix)))

def find_max_volume():
    vectors = []
    idx = []
    for i in range(20):
        max_volume = 0
        max_idx = 0
        for j in range(data.shape[1]):
            subset = vectors[:]
            if i == 0:
                subset = data[:, j:j+1]
            else:
                subset = np.hstack((data[:, j:j+1], vectors))

            candidate_volume = calculate_volume(subset)
            if max_volume < candidate_volume:
                max_volume = candidate_volume
                vectors = subset  # Fix: Update vectors with the correct subset
                max_idx = j  # Fix: Update max_idx with the correct index
        idx.append(max_idx)  # Fix: Store the index in the idx list
    return vectors, idx

df = pd.read_csv('input.csv')
data = df.values

start = time.time()
best_matrix, best_index = find_max_volume()
best_volume = calculate_volume(best_matrix)
end = time.time()

print(best_volume)
print(best_index)
print(end - start)
