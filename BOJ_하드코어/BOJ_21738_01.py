# 특수얼음깨기
# 얼음 2가지 종류 : 빨간얼음 , 투명얼음
# 빨간 얼음 => 특수 얼음 => 지지대 연결 얼음 => 깨지지 않음
# 투명 얼음 => 1개 빨간얼음만 연결만되도 안깨지긴 하지만
#              펭귄이 올라 가있으면 2개이상의 빨간얼음이 연결되어야만함
# 펭귄이 안떨어지게 최대 몇개의 얼음을 깰수있는것인가?
# N제한 328000 지지대 얼음(빨간얼음) N-1
# 그래프
# 최대 깰수있는 얼음의 갯수 펭귄만 남고
# 즉 펭귄이 살아남는 조건은 두개의 지지대가 연결된 얼음들만 깨면되면 된다
# 각 지지대를 깻을경우 나머지 일반얼음연결된 얼음들도 깨진다
# 간선의 가중치는 1이므로 BFS로 펭귄으로부터 떨어진 지지대 얼음을 찾아서 저장해놓는다 거리를
# 가장짧은 거리의 지지대 2개만 남기고 나머지 얼음을 다 깬다 즉
# 전체 노드수에서 2개지지대에 연결된 얼음수를 빼면 된다....
# 그리고 두 얼음간 연결된 간선은 1개뿐이므로 복잡도 N에 가능할듯?

from collections import deque

import sys

si = sys.stdin.readline

N, S, P = map(int, si().split()) # 얼음 블록수, 지지대역할 얼음수, 펭귄위치한얼음번호

graph = [[] for i in range(N+1)]
red_ice = [False]*(N+1)
for i in range(1,S+1):
    red_ice[i] = True
for _ in range(N-1):
    s,e = map(int, si().split())
    graph[s].append(e)
    graph[e].append(s)
candidates = [99999999]*(N+1)
visited = [False]*(N+1)
def bfs(s):
    q = deque()
    q.append((s,0))
    visited[s] = True
    while q:
        cur , dist = q.popleft()
        if red_ice[cur] and candidates[cur] > dist:
            candidates[cur] = dist
        for n in graph[cur]:
            if not visited[n]:
                visited[n] = True
                q.append((n,dist+1))

bfs(P)
candidates.sort() # NlogN
print(N - candidates[0] - candidates[1] - 1)

