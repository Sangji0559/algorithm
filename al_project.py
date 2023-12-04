import time
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv') # 20*10000
dft = df.T # 10000*20

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix @ matrix.T) #20*20
    volume = np.sqrt(abs(det))
    return volume

def sample_matrix(): # 20*20 행렬 만들기
    sampled_row = list(np.argmax(df, axis=1))
    print(sampled_row)
    sampled_column = df.columns[sampled_row]
    sampled_data = df[sampled_column]
    print(sampled_data)
    return sampled_data

def find_max_volume(data):
    max_volume = 0
    for _ in range(1000): 
        sample = data.sample(n=20, replace = False)
        volume = calculate_volume(sample)
        if(max_volume<volume):
            max_volume = volume
            #print(sample)
            
    return max_volume

start_time = time.time()
print(calculate_volume(sample_matrix()))
max_volume = find_max_volume(dft)
end_time = time.time()

print(max_volume)
print("소요 시간:", end_time - start_time, "초")

