import numpy as np
import pandas as pd
import time

def calculate_volume(matrix):
    return np.sqrt(np.abs(np.linalg.det(np.dot(matrix.T, matrix))))

def find_max_volume(matrix):
    included_indices = []
    result_matrix = []
    second_max_matrix = []
    result_indices = []
    second_max_indices = []

    for k in range(20):
        max_subset = []
        second_max_subset = []
        max_volume = 0
        second_max_volume = 0
        max_index = 0
        second_max_index = 0

        for i in range(matrix.shape[1]):
            if i in included_indices:
                continue

            subset = np.hstack((matrix[:, i:i+1], result_matrix)) if k > 0 else matrix[:, i:i+1]
            volume = calculate_volume(subset)

            if max_volume < volume:
                second_max_volume = max_volume
                second_max_subset = max_subset
                second_max_index = max_index

                max_volume = volume
                max_subset = matrix[:, i:i+1]
                max_index = i
            elif second_max_volume < volume:
                second_max_volume = volume
                second_max_subset = matrix[:, i:i+1]
                second_max_index = i

        if k == 0:
            result_matrix = second_max_subset
            result_indices.append(second_max_index)
            second_max_matrix = max_subset
            second_max_indices.append(max_index)
        else:
            result_matrix = np.hstack((max_subset, result_matrix)) if k == 1 else np.hstack((result_matrix, max_subset))
            result_indices.append(max_index)
            second_max_matrix = np.hstack((second_max_subset, second_max_matrix))
            second_max_indices.append(second_max_index)
        included_indices.append(max_index)

    return result_matrix, result_indices

if __name__ == "__main__":
    input_data = pd.read_csv('input.csv')
    input_matrix = input_data.values

    start_time = time.time()
    best_matrix, best_index = find_max_volume(input_matrix)
    best_volume = calculate_volume(best_matrix)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("선택된 인덱스:", best_index)
    print("최고 부피:", best_volume)
    print(f"경과 시간: {elapsed_time} 초")
