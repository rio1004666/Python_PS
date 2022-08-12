from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def in_range(i, j, n, m):
    return 1 <= i <= n and 1 <= j <= m


def make_small_wall(n, m, maze, rows, columns, maze_form):
    for r1, c1, r2, c2 in maze_form:
        d = -1  # (r1, c1) 기준에서 (r2, c2)가 어느 방향인 지 찾기
        for idx, (dr, dc) in enumerate(dirs):
            if r1 + dr == r2 and c1 + dc == c2:
                d = idx
        assert d != -1
        # 동일한 관계의 다른 방들에도 1 써주기
        for i in range(rows):
            for j in range(columns):
                r = i * rows + r1
                c = j * columns + c1
                maze[r][c][d] = 1
    for r2, c2, r1, c1 in maze_form:
        d = -1
        for idx, (dr, dc) in enumerate(dirs):
            if r1 + dr == r2 and c1 + dc == c2:
                d = idx
        assert d != -1
        for i in range(rows):
            for j in range(columns):
                r = i * rows + r1
                c = j * columns + c1
                maze[r][c][d] = 1


def make_big_wall(n, m, maze, rows, columns, maze_form):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for idx, (dr, dc) in enumerate(dirs):
                ni, nj = i + dr, j + dc
                if not in_range(ni, nj, n, m): continue
                # (i, j)랑 (ni, nj)가 인접한 두 격자 관계임
                r1, c1 = (i - 1) // rows + 1, (j - 1) // columns + 1  # (i, j) 변환
                r2, c2 = (ni - 1) // rows + 1, (nj - 1) // columns + 1  # (ni, nj) 변환
                # 둘이 같은 곳으로 변환되면, 같은 방에 있던 애들이니까 big wall이랑 관계 없음
                if r1 == r2 and c1 == c2:
                    continue

                if maze[r1][c1][idx] == 1:  # 변환 이후에 이동이 가능하다면
                    maze[i][j][idx] = 1  # 변환 전에도 이동이 가능하게 해준다


def bfs(n, m, maze, r1, c1, r2, c2):
    dist = [[-1 for _ in range(m + 1)] for __ in range(n + 1)]
    que = deque()
    que.append((r1, c1))
    dist[r1][c1] = 0
    while que:
        r, c = que.popleft()
        for d, (dr, dc) in enumerate(dirs):
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc, n, m): continue
            if dist[nr][nc] != -1: continue
            if maze[r][c][d] == 0: continue
            dist[nr][nc] = dist[r][c] + 1
            que.append((nr, nc))
    return dist[r2][c2]


def solution(rows, columns, maze_form, r1, c1, r2, c2):
    n = rows * rows
    m = columns * columns
    maze = [[[0, 0, 0, 0] for _ in range(m + 1)] for __ in range(n + 1)]
    make_small_wall(n, m, maze, rows, columns, maze_form)
    make_big_wall(n, m, maze, rows, columns, maze_form)
    return bfs(n, m, maze, r1, c1, r2, c2)