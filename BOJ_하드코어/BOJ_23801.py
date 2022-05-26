import sys
import heapq
si = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, si().split())
graph = [[] for _ in range(N+1)]

def dijkstra(start):
    q = []
    dist = [INF] * (N+1)
    heapq.heappush(q, (0,start))
    dist[start] = 0
    while q:
        d, cur = heapq.heappop(q)
        if dist[cur] < d:
            continue
        for next_node,cost in graph[cur]:
            if d + cost < dist[next_node]:
                dist[next_node] = d + cost
                heapq.heappush(q,(d + cost, next_node))
    return dist
for _ in range(M):
    u, v, w = map(int, si().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
X,Z = map(int, si().split())
p = int(si())
stopby = list(map(int, si().split()))


X_dist = dijkstra(X) # 출바지점으로부터 모든 지점까지 최단거리 
Z_dist = dijkstra(Z) # 도착지점으로부터 모든 지점까지 최단거리 
result = INF
for stop in stopby: # 임의 특정지점에서 X와 Z까지의 거리 두개를 합한것의 최솟값을 구함
    result = min(result, X_dist[stop] + Z_dist[stop])

if result == INF:
    print(-1)
else:
    print(result)