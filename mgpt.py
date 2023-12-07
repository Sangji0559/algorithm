import numpy as np
import pandas as pd
import time

def calculate_volume(matrix):
    return np.sqrt(np.abs(np.linalg.det(np.dot(matrix.T, matrix))))

def find_max_volume_greedy(matrix):
    included_indices = []
    result_matrix = np.zeros((matrix.shape[0], 0))

    for _ in range(20):
        max_volume = 0
        max_index = 0

        for i in range(matrix.shape[1]):
            if i in included_indices:
                continue

            volume = calculate_volume(
                np.hstack((result_matrix, matrix[:, i:i+1]))
            )

            if volume > max_volume:
                max_volume = volume
                max_index = i

        included_indices.append(max_index)
        result_matrix = np.hstack((result_matrix, matrix[:, max_index:max_index+1]))

    return result_matrix, included_indices

if __name__ == "__main__":
    input_data = pd.read_csv('input.csv')
    input_matrix = input_data.values

    start_time = time.time()
    best_matrix, best_index = find_max_volume_greedy(input_matrix)
    best_volume = calculate_volume(best_matrix)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("선택된 인덱스:", best_index)
    print("최고 부피:", best_volume)
    print(f"경과 시간: {elapsed_time} 초")
