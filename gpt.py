import pandas as pd
import numpy as np

def calcVolume(mat):
    return np.sqrt(np.abs(np.linalg.det(np.dot(mat, mat.T))))

def maximize_volume(matrix, k):
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)

    # make approx matrix
    approx_matrix = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))

    volume = calcVolume(approx_matrix)

    return volume

# CSV 파일에서 데이터 읽기
inp = pd.read_csv('input.csv', header=None)

matrix = inp.values  # DataFrame을 NumPy 배열로 변환

best_k = 0
max_volume = 0

for k in range(1, 21):
    current_volume = maximize_volume(matrix[:, :100], k)

    if current_volume > max_volume:
        max_volume = current_volume
        best_k = k

print("최대 부피:", max_volume)
print("최적의 k:", best_k)
