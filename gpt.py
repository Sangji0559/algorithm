import time
import pandas as pd
import numpy as np
from scipy.optimize import minimize

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix @ matrix.T)
    volume = np.sqrt(abs(det))
    return -volume  # 부피를 최대화하는 것이 목적이므로 -1을 곱해 최소화 문제로 바꿔줍니다.

def volume_optimization(data):
    # 초기 추정치 (모든 열벡터의 크기를 1로 정규화)
    initial_guess = np.ones(data.shape[1]) / np.linalg.norm(data, axis=0)

    # 제약 조건: 열벡터의 크기는 1이어야 함
    constraints = ({'type': 'eq', 'fun': lambda x: np.linalg.norm(x) - 1})

    # 최적화 수행
    result = minimize(calculate_volume, initial_guess, constraints=constraints)

    # 최적화 결과 출력
    max_volume = -result.fun
    max_volume_vector = result.x
    max_volume_matrix = data * max_volume_vector[:, np.newaxis]

    return max_volume, max_volume_matrix

# 데이터 읽어오기
df = pd.read_csv('input.csv')

# 데이터 전치
dft = df.T

start_time = time.time()

# 최대 부피와 해당 행렬 찾기
max_volume, max_volume_matrix = volume_optimization(dft)

end_time = time.time()

print("최대 부피:", max_volume)
print("최대 부피를 가진 행렬:")
print(max_volume_matrix)
print("소요 시간:", end_time - start_time, "초")
