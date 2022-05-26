# 어느 지점에서 시작해도 상관없지만 한번에 갈수있는 칸수가 가장 긴것 찾기 
import sys
si = sys.stdin.readline
N = 5
a = [si().strip() for _ in range(N)]
visit = [[0 for _ in range(N)] for __ in range(N)]
ans = 1
def dfs(x, y, length, chance, visit):  # x, y 까지 length개의 격자를 밟아온 상태. 방문한 격자들은 visit 배열에 저장
    
    ret = 0
    visit[x][y] = 1
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visit[nx][ny] == 1:
            continue
        if a[x][y] < a[nx][ny]:
            ret = max(ret,dfs(nx, ny, length + 1, chance, visit)+1)
        elif a[x][y] > a[nx][ny] and not chance:
            ret = max(ret,dfs(nx, ny, length + 1, True, visit)+1)
    visit[x][y] = 0
    return ret
for i in range(N):
    for j in range(N):
        ans = max(ans,dfs(i, j, 1, False, visit)+1)
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
