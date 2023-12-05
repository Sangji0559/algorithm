import pandas as pd
import numpy as np
from scipy.optimize import minimize

def calculate_volume(matrix):
    if matrix.ndim == 1:
        matrix = matrix.reshape(1, -1)
    
    det = np.linalg.det(matrix.T @ matrix)
    volume = np.sqrt(abs(det))
    return volume

def constraint(matrix):
    if matrix.ndim == 1:
        matrix = matrix.reshape(1, -1)
    return np.sum(matrix, axis=1) - 1.0

def print_values(matrix):
    print("Objective Function Value:", calculate_volume(matrix))
    print("Constraint Value:", constraint(matrix))

# 데이터 불러오기
df = pd.read_csv('input.csv')  # 20*10000

# 예제: 각 열의 노름이 큰 순서대로 20개의 행 선택
sorted_cols = np.argsort(np.linalg.norm(df, axis=0))

# 행렬의 열벡터 크기를 기준으로 정렬하고, 그에 해당하는 행들을 추출
initial_matrix = df.iloc[:, sorted_cols[-20:]]

# 초기 추정값 (2차원 행렬로 변환)
x0 = initial_matrix.to_numpy().flatten()

# 최적화 문제 정의
constraints = ({'type': 'eq', 'fun': constraint})

# 최적화 알고리즘 변경 ('Powell' 사용)
result = minimize(calculate_volume, x0, constraints=constraints, method='Powell', options={'disp': True})

# 최적화 결과 출력
max_volume = result.fun
optimized_matrix = result.x.reshape(initial_matrix.shape)

# 출력
print("====== 최적화 결과 ======")
print("Optimization Exit Code:", result.message)
print("Optimal Matrix:")
print(optimized_matrix)
print("Max Volume:", max_volume)

# 디버깅을 위한 추가 정보 출력
print("\n====== 디버깅 정보 ======")
print_values(optimized_matrix)
print("Condition number of the matrix:", np.linalg.cond(optimized_matrix))
