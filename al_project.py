import time
import pandas as pd
import numpy as np

df = pd.read_csv('input.csv')
dft = df.T

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix @ matrix.T)
    volume = np.sqrt(abs(det))
    return volume

def find_volume():
    data = pd.DataFrame(2,index=range(3),columns=range(3))
    return data
    

def find_max_volume(data):
    max_volume = 0
    for _ in range(500): 
        sample = data.sample(n=20, replace = False)

        volume = calculate_volume(sample)
        if(max_volume<volume):
            max_volume = volume

    return max_volume

start_time = time.time()

data = find_volume()
print(data.T)
print(calculate_volume(data))
end_time = time.time()

#print("결과: ", max_volume)
#print("소요 시간:", end_time - start_time, "초")
