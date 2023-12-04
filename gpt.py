import pandas as pd
import numpy as np

def calcVolume(mat):
    return np.sqrt(np.abs(np.linalg.det(np.dot(mat, mat.T))))

def maximize_volume(matrix, k):
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)

    # 대각 행렬 직접 생성
    diag_S = np.diag(S[:k])

    # make approx matrix
    approx_matrix = np.dot(U[:, :k], np.dot(diag_S, Vt[:k, :]))

    volume = calcVolume(approx_matrix)

    return volume

# CSV 파일에서 데이터 읽기
inp = pd.read_csv('input.csv', header=None)

matrix = inp.values  # DataFrame을 NumPy 배열로 변환

best_k = 0
max_volume = 0

num_columns_to_use = 300  # 사용할 열 수 조정
current_volume = maximize_volume(matrix[:, :num_columns_to_use], 20)

if current_volume > max_volume:
    max_volume = current_volume

print("최대 부피:", max_volume)
