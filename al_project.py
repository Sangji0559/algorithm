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

def top_sample(matrix):
    v_list=[]
    for col_idx, col in enumerate(matrix.columns):
        vector_size = np.linalg.norm(np.array(matrix[col]))
        v_list.append((vector_size,col_idx))
        v_list.sort(reverse=True)
    return (v_list[0:20])

def find_max_volume(data):
    max_volume = 0
    max_sums = 0
    for _ in range(1000): 
        sample = data.sample(n=20, replace = False)
        volume = calculate_volume(sample)
        if(max_volume<volume):
            max_volume = volume
            #print(sample)
            

            
    return max_volume

start_time = time.time()
#max_volume = find_max_volume(dft)
print(top_sample(df))
end_time = time.time()

#print("결과: ", max_volume)
print("소요 시간:", end_time - start_time, "초")
