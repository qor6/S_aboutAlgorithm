import heapq

def prim(graph, start):
    n = len(graph)
    D = [float('inf')] * n  # D 배열 초기화 (무한대로 설정)
    D[start] = 0  # 시작 정점의 가중치는 0
    min_heap = [(0, start, 0)]  # (가중치, 정점) 형태의 최소 힙을 사용하여 간선을 저장
    visited = [False] * n  # 방문 여부를 저장할 리스트
    tree_edges = []  # 최소 신장 트리를 저장할 리스트

   
    while min_heap:
        weight, current_node, start_node = heapq.heappop(min_heap)   
        if not visited[current_node]:
            visited[current_node] = True
            if current_node != start:
                tree_edges.append((start_node,current_node , D[current_node]))  # 최소 신장 트리에 간선 추가
            for neighbor, neighbor_weight in graph[current_node]:
                if not visited[neighbor] and neighbor_weight < D[neighbor]:
                    D[neighbor] = neighbor_weight  # D 배열 갱신
                    heapq.heappush(min_heap, (neighbor_weight, neighbor, current_node))  # 최소 힙에 간선 추가
    return tree_edges

# 주어진 리스트를 그래프로 변환
input = [(0, 1, 3), (0, 4, 4), (0, 3, 2), (1, 2, 1), (1, 5, 2), (1, 3, 4), (2, 5, 1), (3, 5, 7), (3, 4, 5), (4, 5, 9)]
graph = {}  # 인접 리스트 형태의 그래프를 사용
for u, v, weight in input:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, weight))
    graph[v].append((u, weight))

# 프림 알고리즘 실행 (시작 정점: c)
minimum_spanning_tree = prim(graph, 2)
# 결과 출력
for edge in minimum_spanning_tree:
    print(edge)