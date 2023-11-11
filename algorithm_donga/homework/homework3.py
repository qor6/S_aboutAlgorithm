import time
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    vertices = list(graph.keys())

    while vertices:
        # 최소 거리를 가진 정점 찾기
        current_node = min(vertices, key=lambda node: distances[node])
        vertices.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

def floyd(graph):
    num_nodes = len(graph)
    distances = [[float('inf')] * num_nodes for _ in range(num_nodes)]

    # 초기화: 그래프에서 직접 이동 가능한 경우에는 가중치 값으로 초기화
    for i, node in enumerate(graph):
        distances[i][i] = 0
        for neighbor, weight in graph[node].items():
            distances[i][list(graph).index(neighbor)] = weight

    # 중첩된 루프를 사용한 Floyd 알고리즘
    for k in range(num_nodes):
        for i in range(num_nodes):
            if i == k:
                continue
            for j in range(num_nodes):
                if j == k or j == i:
                    continue
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances

# 그래프 정의
graph = {
    '서울': {'천안': 12, '원주': 15},
    '천안': {'서울': 12, '논산': 4, '대전': 10},
    '원주': {'서울': 15, '강릉': 21, '대구': 7},
    '논산': {'천안': 4, '대전': 3, '광주': 13},
    '대전': {'천안': 10, '논산': 3, '대구': 10},
    '강릉': {'원주': 21, '포항': 25},
    '대구': {'원주': 7, '포항': 19, '부산': 9, '대전': 10},
    '포항': {'강릉': 25, '대구': 19, '부산': 5},
    '부산': {'포항': 5, '대구': 9, '광주': 15},
    '광주': {'논산': 13, '부산': 15}
}

# 실행 시간을 더 정확하게 측정하기 위해 코드를 여러 번 반복 실행
num_iterations = 1

# 다익스트라 알고리즘 실행 시간 측정
start_time = time.time()
for _ in range(num_iterations):
    all_pairs_dijkstra = {}
    for node in graph:
        all_pairs_dijkstra[node] = dijkstra(graph, node)
end_time = time.time()
dijkstra_time = (end_time - start_time) / num_iterations

# Floyd 알고리즘 실행 시간 측정
start_time = time.time()
for _ in range(num_iterations):
    all_pairs_floyd = floyd(graph)
end_time = time.time()
floyd_time = (end_time - start_time) / num_iterations

def print_table(header, data):
    # 출력할 데이터를 테이블 형태로 정리하여 출력하는 함수
    max_label_len = max(map(len, header))
    print(" " * max_label_len, end="\t")
    print("\t".join(header[1:]))

    for row_label, row in zip(header, data):
        print(f"{row_label}\t" + "\t".join(map(lambda x: f"{x:^{max_label_len}}" if x is not None else "", row[1:])))

# 다익스트라 알고리즘 결과 출력
print("Dijkstra Algorithm:")
nodes = list(graph)
header = [""] + nodes
data_dijkstra = [[label] + list(map(all_pairs_dijkstra[label].get, nodes)) for label in nodes]
print_table(header, data_dijkstra)

# Floyd 알고리즘 결과 출력
print("\nFloyd Algorithm:")
data_floyd = [[label] + row for label, row in zip(nodes, all_pairs_floyd)]
print_table(header, data_floyd)

# 실행 시간 출력
print(f"\nDijkstra Algorithm 실행 Time: {dijkstra_time} seconds")
print(f"Floyd Algorithm 실행 Time: {floyd_time} seconds")
