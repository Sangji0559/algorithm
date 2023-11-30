coordinates = [(0,3),(7,5),(6,0),(4,3),(1,0),(5,3),(2,2),(4,1)]

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(points):
    edges = []

    # 좌표간의 거리 계산 및 간선 추가
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
            edges.append((i, j, distance))

    # 거리를 기준으로 간선 정렬
    edges.sort(key=lambda edge: edge[2])

    n = len(points)
    mst = []
    uf = UnionFind(n)

    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

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

mst = kruskal(coordinates)
print(mst)
tsp_path = tsp_from_mst(mst, 0)
tsp=[]
for i in tsp_path:
    if i == 0:
        tsp.append('A')
    if i == 1:
        tsp.append('B')
    if i == 2:
        tsp.append('C')
    if i == 3:
        tsp.append('D')
    if i == 4:
        tsp.append('E')
    if i == 5:
        tsp.append('F')
    if i == 6:
        tsp.append('G')
    if i == 7:
        tsp.append('H')
print("TSP 경로 from MST:", tsp)
