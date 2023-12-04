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
    # 예제: 각 열의 노름이 큰 순서대로 20개의 행 선택
    sorted_cols = np.argsort(np.linalg.norm(df, axis=0))

    # 행렬의 열벡터 크기를 기준으로 정렬하고, 그에 해당하는 행들을 추출
    sorted_data = df.iloc[:, sorted_cols[-20:]]
    max_volume = calculate_volume(sorted_data)
    list_col = list(sorted_cols[-40:])  # 초기값 설정

    for i in range(20):
        for j in range(1000):
            sorted_data_copy = sorted_data.copy()  # 복사본을 사용하여 기존 데이터를 변경하지 않도록 함
            sorted_data_copy = sorted_data_copy.drop(columns=sorted_data_copy.columns[i])
            new_column_data = df.iloc[:, sorted_cols[-20 - j]]
            sorted_data_copy[f'{sorted_cols[-20-j]}'] = new_column_data
            current_volume = calculate_volume(sorted_data_copy)
            if current_volume > max_volume:
                print(j, sorted_cols[-20-j])
                max_volume = current_volume
                list_col = list(sorted_data_copy.columns)

    return max_volume, list_col


start_time = time.time()
max_v , index = sample_matrix_custom()
print("matrix volume: ", max_v)
print("matrix index : ", index)
end_time = time.time()

print("소요 시간:", end_time - start_time, "초")
