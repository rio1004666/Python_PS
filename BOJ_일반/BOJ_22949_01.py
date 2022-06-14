# 1. 미로탐색에 배열 돌리기만 추가 되긴 했지만 방문 체크를 어떻게 해야할까?
# 2. 어떤 자료구조, 알고리즘을 써야할까?
# 3. 시간복잡도는 어떻게 될까? 제한시간 안에 해결할 수 있나?
from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


def region(y, x, k):
    y, x = y // 4 * 4, x // 4 * 4
    return y * k + x


def inrange(y, x, N):
    return 0 <= y and y < N and 0 <= x and x < N


def next_pos(y, x):
    by, bx = y // 4 * 4, x // 4 * 4
    y, x = y % 4, x % 4
    return x + by, 3 - y + bx


# Constant
Dy = (-1, 1, 0, 0)
Dx = (0, 0, -1, 1)

K = int(input())
N = 4 * K
Map = [list(input()) for i in range(N)]
# 각 방향의 모든 값 배열
Rotate_Map = [[['.' for j in range(N)] for i in range(N)] for k in range(4)]
# 모든 이동거리를 기록하는 거리배열 ( dp성질 )
dist = [[[-1 for j in range(N)] for i in range(N)] for k in range(4)]

start_point, end_point = (0, 0), (0, 0)

for i in range(N):
    for j in range(N):
        if Map[i][j] == 'S':
            start_point = (i, j)
            Map[i][j] = '.'
        if Map[i][j] == 'E':
            end_point = (i, j)
            Map[i][j] = '.'

for regiony in range(K):
    for regionx in range(K):
        y, x = regiony * 4, regionx * 4 # 4 x 4 로 묶어서 구역을 정하고
        tmp = []
        for h in range(4): tmp.append(Map[y + h][x:x + 4]) # 4x4구역을 때네서 일단 임시로 셋팅한 후에 로테이션 시킬것이다
        for cnt in range(4):
            for hy in range(4):
                for hx in range(4):
                    Rotate_Map[cnt][y + hy][x + hx] = tmp[hy][hx] # 해당하는 4x4구역의 4가지 방향을 저장한다
            tmp = [list(line) for line in list(zip(*tmp[::-1]))] # 튜플형식으로 셋팅해주는 각 열을 리스트로 다시 전환해줌

# BFS (미로탐색)
Q = deque([(0, *start_point)])
sy, sx = start_point
dist[0][sy][sx] = 0
while Q:
    turn, y, x = Q.popleft()
    current_region = region(y, x, K)

    # Move U, D, L, R
    for dy, dx in zip(Dy, Dx):
        qy, qx = dy + y, dx + x
        next_region = region(qy, qx, K)
        if not inrange(qy, qx, N): continue
        if next_region == current_region:
            if Rotate_Map[turn][qy][qx] == '#': continue # 현재 다음 이동할 곳이 장애물이 없어야한다
            qy, qx = next_pos(qy, qx) # 90도 회전 후 큐의 위치를 재설정한다
            next_turn = (turn + 1) % 4 # 90도 회전한다
            if dist[next_turn][qy][qx] != -1: continue # 회전후의 위치에 이미 방문한적이 있다면 패스한다
            dist[next_turn][qy][qx] = dist[turn][y][x] + 1 # 회전후의 위치에 방문한적이 없다면 그 전위치에서 거리를 늘려가며 방문해준다
            Q.append((next_turn, qy, qx))
        else:
            if Rotate_Map[0][qy][qx] == '#': continue
            qy, qx = next_pos(qy, qx)
            if dist[1][qy][qx] != -1: continue
            dist[1][qy][qx] = dist[turn][y][x] + 1
            Q.append((1, qy, qx))

    # Stay : 제자리에 있을경우 90도 회전하고 좌표도 그대로이다
    next_turn, qy, qx = (turn + 1) % 4, y, x
    # 90도 회전 후에 새로운 좌표로 설정된다
    qy, qx = next_pos(qy, qx)
    if dist[next_turn][qy][qx] == -1:
        dist[next_turn][qy][qx] = dist[turn][y][x] + 1
        Q.append((next_turn, qy, qx))

ans = -1
y, x = end_point
for k in range(4):
    value = dist[k][y][x]
    y, x = next_pos(y, x)
    if value == -1: continue
    if ans == -1:
        ans = value
    elif ans > value:
        ans = value

print(ans)