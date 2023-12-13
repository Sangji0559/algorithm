import heapq

v, e = map(int,input().split()) # 노드 수, 간선 수
visited = [0] * (v+1) # 노드의 방문 정보 초기화
graph = [[] for _ in range(v+1)]  # 그래프 초기화

# 무방향 그래프 생성
for i in range(e): # 간성 정보 입력 받기
    u, v, weight = map(int,input().split())
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])


# 프림 알고리즘
def PrimMST(start):
    visited[start] = 1 # 방문 갱신
    candidate = graph[start] # 인접 간선 추출
    heapq.heapify(candidate) # 우선순위 큐 생성
    mst = [] # mst

    while candidate:
        weight, u, v = heapq.heappop(candidate) # 가중치가 가장 적은 간선 추출
        if visited[v] == 0: # 방문하지 않았다면
            visited[v] = 1 # 방문 갱신
            mst.append((u,v,weight)) # mst 삽입

            for edge in graph[v]: # 다음 인접 간선 탐색
                if visited[edge[2]] == 0: # 방문한 노드가 아니라면, (순환 방지)
                    heapq.heappush(candidate, edge) # 우선순위 큐에 edge 삽입

    return mst

start_node = int(input())
print(PrimMST(start_node))