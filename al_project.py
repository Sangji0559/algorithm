import numpy as np
import pandas as pd
import time

def calculate_volume(matrix):
    return np.sqrt(np.abs(np.linalg.det(np.dot(matrix.T, matrix))))

def find_max_volume(matrix):
    included_indices = []

    sorted_cols = np.argsort(np.linalg.norm(matrix, axis=0))[-100:]

    best_result = None
    best_volume = 0

    for j in range(len(sorted_cols)):
        result_matrix = []
        result_indices = []

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

            if k == 0:
                # sorted_cols의 j번째 열을 선택
                result_matrix = matrix[:, sorted_cols[j]:sorted_cols[j]+1]
                result_indices.append(sorted_cols[j])
            else:
                result_matrix = np.hstack((max_subset, result_matrix)) if k == 1 else np.hstack((result_matrix, max_subset))
                result_indices.append(max_index)
            included_indices.append(max_index)

        # 현재 j에 대한 결과의 부피를 계산
        current_volume = calculate_volume(result_matrix)

        # 현재 결과의 부피가 더 크다면 갱신
        if current_volume > best_volume:
            best_volume = current_volume
            best_result = (j, result_indices)

    return best_result

if __name__ == "__main__":
    input_data = pd.read_csv('input.csv')
    input_matrix = input_data.values

    start_time = time.time()
    best_result = find_max_volume(input_matrix)
    j, result_indices = best_result

    print(f"\nBest Results:")
    print("Selected Indices:", result_indices)
    print("Best Volume:", best_volume)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTotal Elapsed Time: {elapsed_time} seconds")
