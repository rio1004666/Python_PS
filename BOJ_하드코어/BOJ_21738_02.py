# 여기서는 각 얼음에서 dfs탐색 햇다 혹은
# 펭귄부터 dfs 탐색을 할수도 있다


import sys

input = sys.stdin.readline
# 재귀함수 횟수 제한을 늘려줌
sys.setrecursionlimit(329000)

N, S, P = map(int, input().split())
graph = [[] for i in range(N + 1)]

# 각각 얼음이 연결된 관계를 그래프로 저장
for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

iceBroken = []
# 방문한 얼음
visited = [0] * (N+1)


def dfs(n, cnt):
    # 현재 방문한 얼음이 펭귄이 서있는 곳이면
    # 해당 기둥의 연결 얼음 갯수 반환
    if n == P:
        iceBroken.append(cnt)
        return
    visited[n] = 1
    for i in graph[n]:
        # 해당 얼음과 연결된 얼음 탐색
        if not visited[i]:
            dfs(i, cnt + 1)

# 6개의 얼음 기둥 탐색
for i in range(1, S+1):
    dfs(i, 0)

iceBroken.sort()

# 전체 얼음 - 가장 연결갯수가 적은 기둥 2개 - 펭귄이 서있는 얼음
print(N - iceBroken[0] - iceBroken[1] - 1)