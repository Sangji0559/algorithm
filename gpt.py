import heapq

def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance

def calculate_total_distance(coordinates, tsp_path):
    total_distance = 0
    for i in range(len(tsp_path) - 1):
        start_coord = coordinates[tsp_path[i]]
        end_coord = coordinates[tsp_path[i + 1]]
        distance = calculate_distance(start_coord, end_coord)
        total_distance += distance

    return total_distance

coordinates = [(0,3),(7,5),(6,0),(4,3),(1,0),(5,3),(2,2),(4,1)]

visited = [0] * (len(coordinates)) # 노드의 방문 정보 초기화
graph = [[] for _ in range(len(coordinates))]  # 그래프 초기화
edges = []

# 좌표간의 거리 계산 및 간선 추가
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
        edges.append((distance, i, j))

# 무방향 그래프 생성
for i in edges: # 간성 정보 입력 받기
    weight, u, v = i
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

def mst_to_graph(mst_edges):
    graph = {}
    for edge in mst_edges:
        u, v, weight = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    return graph

def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    visit = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            visit.append(node)
            stack.extend(graph[node])

    return visit

def tsp(graph, start_node):
    circuit = dfs(graph, start_node)
    unique_circuit = list(dict.fromkeys(circuit))  # 중복 제거
    unique_circuit += [unique_circuit[0]]
    tsp_path = []
    return tsp_path

mst_g = mst_to_graph(PrimMST(0))
tsp_path = tsp(mst_g, 0)
tsp_distance = calculate_total_distance(coordinates, tsp_path)


print("TSP 경로:", tsp_path)
print("TSP 경로 거리 (calculate_total_distance 함수 사용):", distance)
print("TSP 경로 거리 (calculate_tsp_distance 함수 사용):", tsp_distance)
