import time
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv') # 20*10000
dft = df.T # 10000*20

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix @ matrix.T)
    volume = np.sqrt(abs(det))
    return volume

def sample_matrix(): # 20*20 행렬 만들기
    sampled_col = list(np.argmax(np.abs(df.values), axis=1))
    
    sampled_column = df.columns[sampled_col]
    sampled_data = df[sampled_column]
    
    return sampled_data, sampled_col


start_time = time.time()
data, index = sample_matrix()
print("max_volume : ", calculate_volume(data))
print("matrixindex : ", list(index))
end_time = time.time()
print("소요 시간:", end_time - start_time, "초")