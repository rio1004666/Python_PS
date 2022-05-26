# 상하좌우 인접한 문자가 같은 종류면 묶여있어야한다 (연속해서)
# N,M과 ?의 개수는 9이하이다
# ?의 갯수만 궁금하므로 ?에만 집중한다 => 9개로 작다
# 가능한 모든 경우의 수는 3^(물음표의 갯수) a or b or c 3개중 가능
# 최대 3^9 = 19000....이다 => 충분히 작다 같은 종류끼리 모여있는지만 확인해준다
# 시간복잡도 = 3^(?의갯수) * 군집판단시간(bfs로 확인 => 최대 9*9)
# 즉 1억(기준)을 넘지 않고 160만정도이므로 풀수잇다!
# 즉 완전탐색으로 가능



import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = [list(si().strip()) for _ in range(n)]
visit = [[0 for _ in range(m)] for __ in range(n)]
Qs = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '?':
            Qs.append((i, j))
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
def dfs(x, y):
    visit[x][y] = True
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if visit[nx][ny]: continue
        if a[nx][ny] != a[x][y]: continue
        dfs(nx, ny)
def check_group():
    # 모든 고릴라 종이 하나의 군집을 이루면 True, 아니면 False를 리턴하는 함수
    for i in range(n):
        for j in range(m):
            visit[i][j] = False
    for sp in "GRL":
        cnt = 0  # sp 종의 그룹 개수
        for i in range(n):
            for j in range(m):
                if a[i][j] == sp and not visit[i][j]:
                    cnt += 1
                    dfs(i, j)
        if cnt >= 2:
            return False
    return True
ans = 0
def back(idx):  # 0 ~ idx-1 까지의 물음표 위치에 고릴라 예측했고, idx부터 예측하기
    global ans
    if idx == len(Qs):  # 모든 물음표 예측 완료
        if check_group():
            ans += 1
        return
    for ch in "GRL":
        x, y = Qs[idx]
        a[x][y] = ch
        back(idx + 1)
        a[x][y] = '?'
back(0)
print(ans)






