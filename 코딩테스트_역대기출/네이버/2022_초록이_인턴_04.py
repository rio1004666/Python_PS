import sys

si = sys.stdin.readline
n, m = map(int, si().split())
a = [list(si().strip()) for _ in range(n)]
ans = [0, 0, 0]


def in_range(i, j):
    return 0 <= i < n and 0 <= j < m


dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(n):
    for j in range(m):
        if a[i][j] != 'O': continue
        cnt = 0
        for di, dj in dir:
            ni, nj = i + di, j + dj
            if not in_range(ni, nj):
                continue
            if a[ni][nj] == 'O':
                cnt += 1
        if cnt == 0:  # 1 year old
            ans[0] += 1
            a[i][j] = 'X'

        elif cnt == 2:  # 3 years old
            ans[2] += 1
            for di, dj in dir:
                ni, nj = i + di, j + dj
                if not in_range(ni, nj):
                    continue
                a[ni][nj] = 'X'
            a[i][j] = 'X'
for i in range(n):
    for j in range(m):
        if a[i][j] == 'O':  # one of 2 years old
            ans[1] += 1
ans[1] //= 2
print(*ans)