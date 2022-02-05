
import sys
si = sys.stdin.readline
N = 5
a = [si().strip() for _ in range(N)]
visit = [[0 for _ in range(N)] for __ in range(N)]
ans = 0
def dfs(x, y, length, chance, visit):  # x, y 까지 length개의 격자를 밟아온 상태. 방문한 격자들은 visit 배열에 저장
    global N, ans
    ans = max(ans, length)
    visit[x][y] = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visit[nx][ny] == 1:
            continue
        if a[x][y] < a[nx][ny]:
            dfs(nx, ny, length + 1, chance, visit)
        elif a[x][y] > a[nx][ny] and not chance:
            dfs(nx, ny, length + 1, True, visit)
    visit[x][y] = 0
for i in range(N):
    for j in range(N):
        dfs(i, j, 1, False, visit)
print(ans)
# QBCDE
# PABCF
# OHADG
# NGFEH
# MLKJI
# 25
# ABTTT
# TCDET
# TTTFT
# BAHGF
# CDEFG
# 15
