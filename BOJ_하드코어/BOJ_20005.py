import sys
from collections import deque

m, n, p = map(int, input().split())
info = [sys.stdin.readline().strip() for _ in range(m)]
# ‘.’은 이동할 수 있는 길, ‘X’는 이동할 수 없는길, 알파벳 소문자는 플레이어의 아이디이며 ‘B’는 보스몬스터의 위치

players = {}
for _ in range(p):
    name, dps = sys.stdin.readline().split()
    players[name] = int(dps)

boss_hp = int(input())


# B 보스몬스터 위치 찾기

def boss_coord():
    for i in range(m):
        for j in range(n):
            if info[i][j] == "B": return BFS(i, j) # 보스몬스터로부터 각 플레이어들에게 도착하는 것이 가장 빠르다


def BFS(x, y):
    global boss_hp

    hitter = set()
    visit = [[False] * n for _ in range(m)]
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    q.append((x, y))
    while q:
        for name in hitter:
            boss_hp -= players[name]

        if boss_hp <= 0:
            # print(hitter)
            return len(hitter)

        for time in range(len(q)):  # 1 초     ?? for 문 안에서 q 의 길이가 길어져도 상관 없구나 !!
            node_x, node_y = q.popleft()
            if info[node_x][node_y] not in ".XB":  # 플레이어의 위치에 왔을 경우
                hitter.add(info[node_x][node_y])  # 보스 공격자에 추가

            for i, j in dir:
                new_x, new_y = node_x + i, node_y + j
                if not (0 <= new_x < m and 0 <= new_y < n): continue
                if visit[new_x][new_y]: continue
                if info[new_x][new_y] == "X": continue

                visit[new_x][new_y] = True
                q.append((new_x, new_y))
    return p


print(boss_coord())