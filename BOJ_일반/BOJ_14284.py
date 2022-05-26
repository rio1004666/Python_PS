import heapq
import sys

INF = sys.maxsize
si = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        # d는 now 현재 노드까지의 최소거리
        d, now = heapq.heappop(q)
        print(dist[now])
        # 이미 기록된 거리가 최소라면 더이상 계산할 필요가 없다 ( 이미 방문했다는것을 표시해줌  visited체크 대신 사용 )
        # 현재 노드에 기록된 비용(거리)보다 크다면 패스한다 왜냐 현재노드에 방문하는 거리들이 힙큐에서 쭉나올것이기때문이다 (여러곳에서 현재노드를 방문하므로)
        if dist[now] < d:
            continue
        for v , w in graph[now]:
            cost = d + w
            # 다음노드에 기록된 최소비용보다 작다면 갱신해준다
            if cost < dist[v]:
                dist[v] = cost

                heapq.heappush(q,(cost,v))

N,M = map(int, si().split())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)
for _ in range(M):
    a, b, c  = map(int, si().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
s,t = map(int, si().split())
dijkstra(s)
# 도착지점
print(dist[t])
