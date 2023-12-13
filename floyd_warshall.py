import time # 실 실행시간 측정을 위한 타임 모듈 추가
INF = int(1e9) # 무한대 설정

n,m = map(int, input().split())  # 정점의 개수(n), 간선의 개수(m) 입력
graph = [[INF]*(n+1) for _ in range(n+1)] # 그래프는 2차원 배열로 길이를 저장

for i in range(1,n+1):
  graph[i][i]=0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c
  graph[b][a] = c # 양방향으로 그래프 가중치 입력

start = time.time()

# 플로이드 워셜 알고리즘
for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if i!=j:
        graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

# 완료한 배열을 출력
for i in range(1, n+1):
  graph[i][i]=0
  for j in range(1, n+1):
    if i<=j:
      if graph[i][j] == INF:
          print(" X", end='')
      else:
          print('%2d' % (graph[i][j]),end=' ')
    else:
      print(" X", end=" ")
  print()

end=time.time()
print(end-start)