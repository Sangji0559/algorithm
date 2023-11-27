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
    sample = data.sample(frac=0.3)
    volume = calculate_volume(sample)
    return volume

start_time = time.time()
for _ in range(100):
    max_volume=0
    fvolume = find_max_volume(dft)
    if(max_volume<fvolume):
        max_volume=fvolume
end_time = time.time()

print("단위 벡터 결과:")
print(max_volume)
print("소요 시간:", end_time - start_time, "초")
