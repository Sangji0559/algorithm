import time
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')  # 20*10000
dft = df.T  # 10000*20

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix.T @ matrix)
    volume = np.sqrt(abs(det))
    return volume

def sample_matrix_custom():
    # 예제: 각 열의 합이 큰 순서대로 20개의 행 선택
    col_sums = df.abs().sum(axis=0)
    sampled_cols = col_sums.nlargest(1000).index
    sampled_data = df[sampled_cols]
    print(sampled_data)
    sampled_col = list(np.argmax(np.abs(sampled_data.values), axis=1))
    sampled_column = df.columns[sampled_col]
    sampled_data = df[sampled_column]
    print(sampled_data)
    
    return sampled_data, sampled_col


start_time = time.time()
print("sample_matrix_custom 결과: ", calculate_volume(sample_matrix_custom()))
end_time = time.time()

print("소요 시간:", end_time - start_time, "초")
