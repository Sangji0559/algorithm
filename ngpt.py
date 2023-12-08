import numpy as np
import pandas as pd
import time

def calculate_volume(matrix):
    return np.sqrt(np.abs(np.linalg.det(np.dot(matrix.T, matrix))))

def find_max_volume(matrix,j):
    included_indices = []
    result_matrix = []
    result_indices = []
    
    sorted_cols = []

    for k in range(20):
        max_subset = []
        max_volume = 0
        max_index = 0

        for i in range(matrix.shape[1]):
            if i in included_indices:
                continue

            subset = np.hstack((matrix[:, i:i+1], result_matrix)) if k > 0 else matrix[:, i:i+1]
            volume = calculate_volume(subset)

            if max_volume < volume:
                max_volume = volume
                max_subset = matrix[:, i:i+1]
                max_index = i
                sorted_cols.append(i)

        if k == 0:
            # sorted_cols의 첫 번째 열을 선택
            result_matrix = matrix[:, sorted_cols[-j]:sorted_cols[-j]+1]
            result_indices.append(sorted_cols[-j])
        else:
            result_matrix = np.hstack((max_subset, result_matrix)) if k == 1 else np.hstack((result_matrix, max_subset))
            result_indices.append(max_index)
        included_indices.append(max_index)

    return result_matrix, result_indices

if __name__ == "__main__":
    input_data = pd.read_csv('input.csv')
    input_matrix = input_data.values
    start_time = time.time()
    max_v = 0
    max_i = 0
    for i in range(1):
        best_matrix, best_index = find_max_volume(input_matrix,i)
        best_volume = calculate_volume(best_matrix)
        if max_v < best_volume:
            max_idx = best_index
            max_v = best_volume
    end_time = time.time()
    print(max_idx[0])
    print(max_v)
    print(max_idx)
    elapsed_time = end_time - start_time
    print(f"경과 시간: {elapsed_time} 초")


