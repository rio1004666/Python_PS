
"""
이베이코리아 3번 문제

"""

def shift(grid):
    n = len(grid)
    res = []
    for idx, row in enumerate(grid):
        res.append([None for _ in range(n * 2 - 1)])
        for i in range(n - idx - 1, n + idx):
            res[idx][i] = row[i - (n - idx - 1)]
    return res
def solution(grid):
    def inRange(r, c):
        nonlocal grid
        n = len(grid)
        if r < 0 or r >= n: return False
        if c < n - r - 1 or c >= n + r: return False
        return True
    def traverse(r, c, port):
        nonlocal con, conv, grid
        res = 0
        while inRange(r, c):
            res += 1
            port = conv[grid[r][c]][port]
            r, c, port = con[r][c][port]
        return res
    # inside rule
    conv = dict()
    conv['R'] = [0 for _ in range(6)]
    conv['B'] = [0 for _ in range(6)]
    conv['R'][0], conv['R'][2], conv['R'][4] = 5, 1, 3
    conv['B'][0], conv['B'][2], conv['B'][4] = 3, 5, 1
    # connection
    n = len(grid)
    con = [[[(-1, -1, -1) for _ in range(6)] for _ in range(n * 2 - 1)] for _ in range(n)]
    grid = shift(grid)
    for r in range(n):
        for c in range(n - r - 1, n + r):
            if (r + c) % 2 == (n - 1) % 2:  # right triangle
                con[r][c][1] = (r, c + 1, 4)
                con[r][c][3] = (r + 1, c, 0)
                con[r][c][5] = (r, c - 1, 2)
            else:  # inverse triangle
                con[r][c][1] = (r - 1, c, 2)
                con[r][c][3] = (r, c + 1, 4)
                con[r][c][5] = (r, c - 1, 0)
    answer = 0
    for r in range(n):
        # left side
        answer = max(answer, traverse(r, n - r - 1, 4))
        # right side
        answer = max(answer, traverse(r, n + r - 1, 0))
    # bottom side
    for c in range(0, n * 2 - 1, 2):
        answer = max(answer, traverse(n - 1, c, 2))
    return answer