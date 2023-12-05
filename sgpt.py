import pandas as pd
import numpy as np
from scipy.optimize import minimize

def calculate_volume(matrix):
    det = np.linalg.det(matrix.T @ matrix)
    volume = np.sqrt(abs(det))
    return -volume

def constraint(matrix):
    return np.sum(matrix, axis=1) - 1.0

def optimize_matrix_volume(initial_matrix):
    # 초기 추정값 (2차원 행렬로 변환)
    x0 = initial_matrix.to_numpy().flatten()

    # 최적화 문제 정의
    constraints = ({'type': 'eq', 'fun': constraint})
    result = minimize(calculate_volume, x0, constraints=constraints)

    # 최적화 결과 출력
    max_volume = -result.fun
    optimized_matrix = result.x.reshape(initial_matrix.shape)
    
    return max_volume, optimized_matrix

# 데이터 불러오기
df = pd.read_csv('input.csv')  # 20*10000

# 예제: 각 열의 노름이 큰 순서대로 20개의 행 선택
sorted_cols = np.argsort(np.linalg.norm(df, axis=0))

# 행렬의 열벡터 크기를 기준으로 정렬하고, 그에 해당하는 행들을 추출
initial_matrix = df.iloc[:, sorted_cols[-20:]]

# 최대 부피를 갖는 행렬 찾기
max_volume, optimized_matrix = optimize_matrix_volume(initial_matrix)

print("최대 부피를 갖는 행렬:")
print(optimized_matrix)
print("최대 부피:", max_volume)
