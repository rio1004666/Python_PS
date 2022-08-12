import sys
from collections import deque
si = sys.stdin.readline

# T = [0, 0, 0, 0, 2, 3, 3]
# A = [2, 5, 6]

T = [0, 3, 0, 0, 5, 0, 5]
A = [4, 2, 6, 1, 0]

# T = [0, 0, 1 , 2]
# A = [1,2]

N = len(T)
M = len(A)

graph = [[] for _ in range(N)]
reversed_graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]


# 빨간스킬들의 "배워야할 스킬"들을 탐색하러 간다

def BFS(start):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for nxt in reversed_graph[cur]:
            if visited[nxt]:continue
            visited[nxt] = True
            q.append(nxt)

# 그래프를 연결한다

for i in range(1, N):
    graph[T[i]].append(i)

# 모든 간선을 거꾸로 한다

for i in range(N):
    for nxt in graph[i]:
        reversed_graph[nxt].append(i)
print(reversed_graph)

# 각각에 빨간정점으로부터 BFS탐색하면서 부모노드들을 전부 방문표시한다

for i in range(M):
    # 빨간정점 하나씩 꺼내서 bfs탐색시킨다
    start = A[i]
    BFS(start)
answer = 0
for checked in visited:
    if checked:
        answer += 1
print(answer)