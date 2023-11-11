class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(edges):
    edges.sort(key=lambda x: x[2])  # 간선을 가중치에 따라 정렬
    n = len(edges)
    mst = []  # 최소 신장 트리를 저장할 리스트
    uf = UnionFind(n)

    for edge in edges:
        u, v, weight = edge
        if uf.find(u) != uf.find(v):
            mst.append(edge)
            uf.union(u, v)
    return mst

# 주어진 리스트를 간선 형태로 변환
# a:0 / b:1 / c:2 / d:3 / e:4 / f:5
input = [(0,1,8), (0,4,4), (0,3,2), (1,2,1), (1,5,2), (1,3,4), (2,5,1), (3,5,7), (3,4,3),(4,5,9)]
edges = [(u, v, weight) for u, v, weight in input]

# 크루스칼 알고리즘 실행
minimum_spanning_tree = kruskal(edges)

# 결과 출력
for edge in minimum_spanning_tree:
    print(edge)