import time
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')
dft=df.T

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix.T @ matrix)
    volume = np.sqrt(abs(det))
    return volume

def find_max_volume(data):
    max_volume = 0
    for _ in range(100):
        sample = data.sample(frac=0.3)
        volume = calculate_volume(sample)
        if(max_volume<volume):
            max_volume = volume
    
    return max_volume
    

start_time = time.time()
max_volume = find_max_volume(dft)
end_time = time.time()

print("단위 벡터 결과:")
print(max_volume)
print("소요 시간:", end_time - start_time, "초")
