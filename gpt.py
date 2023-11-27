import pandas as pd
import numpy as np
import random
import time

def calculate_volume(matrix):
    # 행렬의 부피 계산
    det = np.linalg.det(matrix.T @ matrix)
    volume = np.sqrt(abs(det))
    return volume

m = 500  # 원하는 샘플 개수

# '0' 열을 기준으로 샘플링
sampled_data = input_data['0'].sample(m, replace=False).values


def find_max_volume(input_file, m, num_samples):
    # CSV 파일에서 데이터 로드
    data = pd.read_csv(input_file)
    
    start_time = time.time()
    
    max_volume = 0
    max_index = None
    
    for _ in range(num_samples):
        print("h")
        # 무작위로 샘플된 인덱스 (전체 집합 크기보다 작거나 같도록 설정)
        sample_indices = random.sample(range(data.shape[0]), min(m, data.shape[0]))
        
        # 행렬 A 구성
        A = data.iloc[sample_indices, 1:].values
        
        # 볼륨 계산
        volume = calculate_volume(A)
        
        # 최대 볼륨 갱신
        if volume > max_volume:
            max_volume = volume
            max_index = sample_indices
    
    end_time = time.time()
    
    # 결과 출력
    print(f"최대 볼륨: {max_volume}")
    print(f"해당 벡터의 인덱스: {max_index}")
    print(f"실행 시간: {end_time - start_time} 초")

# 입력 파일 경로
input_file_path = 'input.csv'

# 추출할 벡터의 개수 (예: 50개)
m = 10

# 샘플링 횟수 (조절 가능)
num_samples = 1000

# 함수 호출
find_max_volume(input_file_path, m, num_samples)
