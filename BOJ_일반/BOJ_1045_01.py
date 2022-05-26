import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
pq = []
parents = [i for i in range(n)]

for i in range(n):
    row = list(sys.stdin.readline().rstrip())
    for j in range(i+1, n):
        if row[j] == 'Y': heapq.heappush(pq, [i, j])
        # i < j인 간선만 입력

def find(node):
    if parents[node] == node: return node
    else:
        parents[node] = find(parents[node])
        return parents[node]
def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2: return False
    else:
        parents[root2] = root1
        return True

if len(pq) < m: print(-1)
# 총 간선의 수가 m보다 적다면 문제 구현 불가능
else:
    answer = [0 for _ in range(n)]
    # m개의 간선을 우선순위에 따라 추가할 때 MST를 만들 때까지 나온 노드의 횟수 카운트
    # + 간선 개수가 총 m개까지 나올 때까지 나온 각 노드 개수 추가
    edge_num = 0
    pq2 = []
    while pq:
        node1, node2 = heapq.heappop(pq)
        if union(node1, node2):
            answer[node1] += 1
            answer[node2] += 1
            edge_num += 1
        else:
            heapq.heappush(pq2, [node1, node2])
    # 크루스칼 알고리즘을 통해 MST에 각 노드 연결 횟수 카운트
    if edge_num != n-1: print(-1)
    # MST가 아닐 때에는 정답 X
    else:
        for _ in range(m-edge_num):
            # MST를 만들고 추가 가능한 간선의 개수만큼 (즉 연결한 간선의 수는 총 m개여야 한다) 추가
            node1, node2 = heapq.heappop(pq2)
            answer[node1] += 1
            answer[node2] += 1
        print(*answer)