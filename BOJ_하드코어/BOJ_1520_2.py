# 백준 1520번 내리막 길
from sys import stdin
from collections import deque
from heapq import heappush, heappop, heapify
input = stdin.readline
m, n = map(int, input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int, input().split())))

count = 0

# 동 남 서 북
dx = [0, +1, 0, -1]
dy = [+1, 0, -1, 0]
visited = [[0]*n for _ in range(m)]
def bfs(now, x, y):
    q = []
    heapify(q)
    global count
    global matrix
    global visited
    visited[x][y] = 1
    heappush(q, (-now, x, y))
    while q:
        now, x, y = heappop(q)
        now *= -1
        if x == m-1 and y == n-1:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                temp = matrix[nx][ny]
                if temp < now:    # 더 낮은 계단칸
                    if visited[nx][ny] == 0:
                        heappush(q, (-temp, nx, ny))
                    visited[nx][ny] += visited[x][y]
    return

bfs(matrix[0][0], 0, 0)
print(visited[m-1][n-1])