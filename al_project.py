import time
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix.T @ matrix)
    volume = np.sqrt(abs(det))
    return volume

def find_max_volume(data):
    max_volume=0

    for _ in range(1000):
        print("h")
        # '0' 열을 기준으로 샘플링
        sampled_data = np.random.choice(data[:'0'],50,replace=False)
        volume = calculate_volume(sampled_data)
        # 최대 볼륨 갱신
        if volume > max_volume:
            max_volume = volume



start_time = time.time()
find_max_volume(df.to_numpy())
end_time = time.time()

print("단위 벡터 결과:")
print(max_volume)
print("소요 시간:", end_time - start_time, "초")
