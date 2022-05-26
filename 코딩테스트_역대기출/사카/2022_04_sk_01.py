# 8x8격자에서 병사가 놓임
# 대각선에 있는 병사들은 그 병사에 의해 보호가 됨
# 각 병사들은 대각선에 있는 병사들을 보호함!
# n개의 병사가 주어지고 (<=64)
# 보호받지 못한 병사들의 갯수 구함
# 총 64개에서 - 보호받은 병사들의 수 = 보호받지 못한 병사들의 수
# 생각의 흐름 => 진짜 보호받는 병사들을 체크함
# 1
# C3
# => 52
import sys

si = sys.stdin.readline
n = int(si())
a = [[0 for _ in range(10)] for __ in range(10)]
for _ in range(n):
    coord = si().strip()  # 병사의 좌표, D7 => 4행 7열
    row = ord(coord[0]) - ord('A') + 1
    col = int(coord[1])
    dirs = [[-1, -1], [1, -1]]
    for dr, dc in dirs:
        for len in range(-7, 8):
            nr = row + dr * len
            nc = col + dc * len
            if 1 <= nr <= 8 and 1 <= nc <= 8:
                a[nr][nc] = 1

ans = 0
for i in range(1, 9):
    for j in range(1, 9):
        if a[i][j] == 0:
            ans += 1

print(ans)


