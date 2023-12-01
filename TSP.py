import networkx as nx
from networkx.algorithms.approximation import min_weighted_dominating_set
from networkx.algorithms import euler

def christofides_tsp(points):
    # Step 1: MST 생성
    G = nx.Graph()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            G.add_edge(i, j, weight=distance)

    mst = nx.minimum_spanning_tree(G)

    # Step 2: 홀수 차수 정점 찾기
    odd_degree_nodes = [node for node, degree in mst.degree if degree % 2 == 1]

    # Step 3: 최소 비용 매칭 생성
    complete_graph = nx.complete_graph(odd_degree_nodes)
    min_weighted_matching = nx.min_weighted_matching(complete_graph)

    # Step 4: 오일러 회로 구성
    eulerian_circuit = list(euler.eulerian_circuit(mst))

    # Step 5: 최종 경로 생성
    final_path = []
    for u, v in eulerian_circuit:
        final_path.append(u)
    final_path = list(dict.fromkeys(final_path))  # 중복 제거

    # Print or use final_path as needed
    tsp_path = []
    for i in final_path:
        if i == 0:
            tsp_path.append('A')
        elif i == 1:
            tsp_path.append('B')
        elif i == 2:
            tsp_path.append('C')
        elif i == 3:
            tsp_path.append('D')
        elif i == 4:
            tsp_path.append('E')
        elif i == 5:
            tsp_path.append('F')
        elif i == 6:
            tsp_path.append('G')
        elif i == 7:
            tsp_path.append('H')

    return tsp_path

# Example usage with your coordinates
coordinates = [(0, 3), (7, 5), (6, 0), (4, 3), (1, 0), (5, 3), (2, 2), (4, 1)]
tsp_path = christofides_tsp(coordinates)
print("Christofides TSP 경로:", tsp_path)
