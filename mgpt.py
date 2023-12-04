import time
import pandas as pd
import numpy as np
from itertools import combinations

df = pd.read_csv('input.csv')  # 20*10000
dft = df.T  # 10000*20

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix.T @ matrix)
    volume = np.sqrt(abs(det))
    return volume

def sample_matrix_custom():
    # 예제: 각 열의 절댓값 합이 큰 순서대로 2000개의 행 선택
    sorted_cols = np.argsort(np.abs(df).sum(axis=0))
    top_2000_cols = sorted_cols[-24:]

    # 모든 가능한 20개 열의 조합을 생성
    combinations_20 = list(combinations(top_2000_cols, 20))

    max_volume = 0
    best_combination = None

    for comb in combinations_20:
        temp_data = df.iloc[:, list(comb)]
        current_volume = calculate_volume(temp_data)
        
        if current_volume > max_volume:
            max_volume = current_volume
            best_combination = list(comb)

    return max_volume, best_combination

start_time = time.time()
max_v, index = sample_matrix_custom()
print("matrix volume: ", max_v)
print("matrix index : ", index)
end_time = time.time()

print("소요 시간:", end_time - start_time, "초")
