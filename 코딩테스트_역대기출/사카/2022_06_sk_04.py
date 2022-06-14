import sys
from collections import deque

si = sys.stdin.readline
n, m, K = map(int, si().split())
grid = [si().strip() for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
que = deque()
que.append((0, 0, K))
dist = [[[100000 for _ in range(K + 1)] for __ in range(m)] for ___ in range(n)]
dist[0][0][K] = 0
while que:
    x, y, oil = que.popleft()
    # 인접한 칸들로 이동 (가중치 0인 간선)
    for dx, dy in dirs:
        nx, ny, n_oil = x + dx, y + dy, oil - 1
        if not in_range(nx, ny): continue
        if oil == 0: continue
        if dist[nx][ny][n_oil] <= dist[x][y][oil]: continue
        if grid[nx][ny] == 'M': continue
        que.appendleft((nx, ny, n_oil))
        dist[nx][ny][n_oil] = dist[x][y][oil]

    # 기름 채우는 이동 (가중치 1인 간선)
    if grid[x][y] == 'O' and dist[x][y][K] > dist[x][y][oil] + 1:
        dist[x][y][K] = dist[x][y][oil] + 1
        que.append((x, y, K))
print(min(dist[n - 1][m - 1]))
