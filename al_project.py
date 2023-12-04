import time
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv') 
dfv = df.values 

def calculate_volume(matrix):
    # 행렬의 부피 계산
    return np.sqrt(abs(np.linalg.det(matrix @ matrix.T)))

def find_max_volume(matrix, k):
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)
    approx_matrix = np.dot(U[:,:k],np.dot(np.diag(S[:k]),Vt[:k,:]))
    volume = calculate_volume(approx_matrix)

    return volume
max_volume = 0

start_time = time.time()
cur_volume = find_max_volume(dfv[:,:10000],20)
if cur_volume > max_volume:
    max_volume = cur_volume
end_time = time.time()

print(max_volume)
print("소요 시간:", end_time - start_time, "초")

