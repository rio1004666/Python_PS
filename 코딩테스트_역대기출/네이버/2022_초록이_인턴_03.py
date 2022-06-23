# 로봇 시뮬레이션 => 현실세계에서 사람이 움직이는 것처럼 컴퓨터세계에서 객체가 움직이는 현상
# 무한 반복하는 구간에 밟은 총 칸수
# 4가지의 방향까지 방문한것인지 체크하려면 3번째 방향인덱스가 필요함 각 칸마다
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = [si().strip() for _ in range(n)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visit =[[[0, 0, 0, 0] for _ in range(m)] for __ in range(n)]
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m
def move(x, y, d):
    for _ in range(4):
        nx, ny = x + dir[d][0], y + dir[d][1]
        if in_range(nx, ny) and a[nx][ny] == '.':
            return nx, ny, d
        d = (d + 1) % 4 # 시계방향으로 회전하기 위한 스킬
    return x, y, d
x, y, d = 0, 0, 0
while True:
    if visit[x][y][d] == 1: # 그 칸에 다시 같은 방향에 방문했었다면 더이상 볼필요도 없음 무한 반복임
        break
    visit[x][y][d] = 1
    x, y, d = move(x, y, d)
ans = 0
for i in range(n):
    for j in range(m):
        v = sum(visit[i][j]) # 같은칸을 여러번 밟아도 한칸으로 치므로 ans += 1로 친다
        if v > 0:
            ans += 1
print(ans)