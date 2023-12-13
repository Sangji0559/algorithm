G = { # 그래프
    'vertices' : [], # 그래프의 정점
    'edges': [] # 그래프의 간선
}

parent = dict() # 부모노드
rank = dict() # 랭크

def initial(node):
  parent[node] = node # 처음 노드의 부모노드 설정
  rank[node] = 0 # 처음 노드의 랭크 설정

def find(node):
  if parent[node] != node: # 부모노드가 node가 아닐 경우
    parent[node] = find(parent[node]) # 부모 노드를 찾아 저장
  return parent[node]

def union(node_a, node_b):
  root_a = find(node_a)
  root_b = find(node_b)
  if rank[root_a]>rank[root_b]:
    parent[root_b] = root_a
  else:
    parent[root_a] = root_b
    if rank[root_a] == rank[root_b]:
      rank[root_b]+=1


def KruskalMST(G):
  mst = []
  for node in G['vertices']:
    initial(node)
  e = G['edges']
  e.sort(key=lambda x : x[2])

  for edge in e:
    node_a, node_b, weight = edge
    if find(node_a) != find(node_b):
      union(node_a,node_b)
      mst.append(edge)

  return mst

v, e = map(int,input().split()) # 노드 수, 간선 수
for i in range(v):
  G['vertices'].append(i)

for i in range(e):
  u, v, weight = map(int, input().split())
  G['edges'].append((u,v,weight))

KruskalMST(G)