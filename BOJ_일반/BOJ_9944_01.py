# 4방향
# 장애물, 보드의 경계, 이미 공이 지나갔던 곳 전까지 계속 이동
# 공이 더이상 이동할 수 없을 때 끝남
# 모든 빈 칸을 공이 방문해야함
# 최소 이동 횟수는 1000000개를 넘지 않는다.

# 출력: 모든 빈 칸을 방문하는 최소 이동 횟수 ('Case 1: 숫자')

# 최솟값을 구하므로 백트래킹 하고 가지치기 할 수 있을 것
# 모든 가능한 좌표에서 시작하여 백트래킹
# 최소 이동 횟수를 1000001로 두고 백트래킹을 모두 마친 후에도 그대로면 -1로.

import sys

sys.setrecursionlimit(1000001)


def BT(y, x, val):
    global move, N, M, left
    if val >= move: return

    changed = []

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        while 0 <= ny < N and 0 <= nx < M and field[ny][nx] == '.':
            field[ny][nx] = '&'
            left -= 1
            changed.append((ny, nx))
            ny += dy[i]
            nx += dx[i]

        # with open('./example.txt', 'a') as f:
        #     f.write(f'y: {y}, x: {x}\n')
        #     f.write(f'{ny - dy[i]}, {nx - dx[i]}, {i}\n')
        #     f.write(f'left: {left}, changed: {len(changed)}\n')
        #     for _ in range(len(field)):
        # print(*field[_])
        # f.write(f'{field[_]}\n')
        # print(ny - dy[i], nx - dx[i], i)

        if changed:
            BT(ny - dy[i], nx - dx[i], val + 1)

        for _ in range(len(changed)):
            cy, cx = changed.pop()
            field[cy][cx] = '.'
            left += 1

    if not left:
        move = min(move, val)


start = 1
while True:
    try:
        N, M = map(int, input().split())
        left = 0
        field = [['.' for i in range(M)] for j in range(N)]

        for i in range(N):
            inp = list(input())
            for j in range(len(inp)):
                if inp[j] == '*':
                    field[i][j] = '*'
                else:
                    left += 1

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]
        move = 1000001

        for i in range(N):
            for j in range(M):
                if field[i][j] == '.':
                    field[i][j] = '&'
                    left -= 1
                    BT(i, j, 0)
                    field[i][j] = '.'
                    left += 1

        if move == 1000001: move = -1

        print('Case {0}: {1}'.format(start, move))
        start += 1
    except EOFError:
        break