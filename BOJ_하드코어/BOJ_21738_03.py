import sys

si = sys.stdin.readline
sys.setrecursionlimit(330000)
N,S,P = map(int, si().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    s,e = map(int, si().split())
    graph[s].append(e)
    graph[e].append(s)

is_red_ice = [False]*(N+1) #  특수한 얼음인가 판단하는 배열
for i in range(1,S+1):
    is_red_ice[i] = True
brokenCnt = [99999999] * (N+1) # 각 깨진 얼음수를 세는 배열
visited = [False] * (N+1) # 방문한곳은 다시 방문하지 않음

def DFS(cur, broken):
    if is_red_ice[cur]:
        brokenCnt[cur] = broken
        return
    visited[cur] = True
    for n in graph[cur]:
        if not visited[n]:
            visited[n] = True
            DFS(n,broken + 1)

DFS(P,0)
# 여기서도 전체에서 2가지의 최소 얼음갯수 경우의 수를 뺀것을 출력하는 것으로 풀이한다
brokenCnt.sort()
print(N-brokenCnt[0]-brokenCnt[1]-1)