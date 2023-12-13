import time # 실 실행시간 측정을 위한 타임 모듈 추가

INF=int(1e9) # 무한대 설정
n, m = map(int, input().split()) # 정점의 개수(n), 간선의 개수(m) 입력

graph = [[INF] * n for _ in range(n)] # 그래프는 2차원 배열로 길이를 저장

for _ in range(m):
  u, v, w = map(int,input().split())  # 출발 정점(u), 도착 정점(v), 가중치(w)
  graph[u - 1][v - 1] = w
  graph[v - 1][u - 1] = w  # 양방향으로 가중치를 추가

start = time.time() # 처음 실행 시간

def dijkstra(graph, start): # 그래프와 시작 정점을 입력받고
  n = len(graph)
  dist = [INF] * n
  dist[start] = 0
  visited = [False] * n # 다른 정점의 방문 리스트를 설정

  for i in range(n):
    min_dist = INF
    min_index = -1

    for j in range(n):
      if not visited[j] and dist[j] < min_dist:
          min_dist = dist[j]
          min_index = j

    visited[min_index] = True # 방문을 했으면 리스트 설정

    for j in range(n):
      if not visited[j] and graph[min_index][j] != INF:
         new_dist = dist[min_index] + graph[min_index][j]
         if new_dist < dist[j]:
            dist[j] = new_dist

  return dist # 길이 리스트 반환

# 각 정점에서 모든 다른 정점까지의 최단 경로 계산
for i in range(n):
  shortest_paths = dijkstra(graph, i)
  for j, distance in enumerate(shortest_paths):
    if j>=i:
      if distance == INF:
          print(" X", end='')
      else:
          print('%2d' % distance,end=' ')
    else:
      print(' X',end=' ')
  print()
end=time.time() # 실행을 마친 시간
print(end-start) # 실행 시간 출력