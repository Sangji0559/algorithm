import heapq

coordinates = [(0,3),(7,5),(6,0),(4,3),(1,0),(5,3),(2,2),(4,1)]

def prim(points):
    n = len(points)
    visited = [False] * n
    heap = [(0, 0)]  # (weight, vertex)
    mst = []

    while heap:
        weight, u = heapq.heappop(heap)

        if not visited[u]:
            visited[u] = True
            for v in range(n):
                if not visited[v]:
                    x1, y1 = points[u]
                    x2, y2 = points[v]
                    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    heapq.heappush(heap, (distance, v))
                    mst.append((u, v, distance))

    return mst

def mst_to_graph(mst_edges):
    graph = {}
    for edge in mst_edges:
        u, v, weight = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    return graph

def tsp_from_mst(mst_edges, start):
    mst_graph = mst_to_graph(mst_edges)

    # Eulerian circuit 찾기
    euler_circuit = []

    def dfs(node):
        nonlocal euler_circuit
        for neighbor, _ in mst_graph[node]:
            if (node, neighbor) not in euler_circuit and (neighbor, node) not in euler_circuit:
                euler_circuit.append((node, neighbor))
                dfs(neighbor)

    dfs(start)

    # 중복되는 도시 제거하고 경로 구성
    tsp_path = [euler_circuit[0][0]]
    for _, v in euler_circuit:
        tsp_path.append(v)

    unique_tsp_path = list(dict.fromkeys(tsp_path))

    return unique_tsp_path

prim_mst = prim(coordinates)

tsp_path_prim = tsp_from_mst(prim_mst, 0)
tsp_prim = []
for i in tsp_path_prim:
    if i == 0:
        tsp_prim.append('A')
    if i == 1:
        tsp_prim.append('B')
    if i == 2:
        tsp_prim.append('C')
    if i == 3:
        tsp_prim.append('D')
    if i == 4:
        tsp_prim.append('E')
    if i == 5:
        tsp_prim.append('F')
    if i == 6:
        tsp_prim.append('G')
    if i == 7:
        tsp_prim.append('H')
print("Prim TSP 경로:", tsp_prim)
