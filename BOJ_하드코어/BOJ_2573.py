import sys
from collections import deque
si = sys.stdin.readline

N,M = map(int, si().split())
graph = [list(map(int, si().split())) for _ in range(N)]
dx,dy = [-1,1,0,0], [0,0,-1,1]
queue = deque()
day = 0
check = False
def bfs(a,b):
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                elif graph[nx][ny] == 0:
                    # 근처에 있는 바다의 갯수를 카운팅하는 count 2차원배열을 따로 저장한다
                    count[x][y] += 1
    # 한번 BFS탐색후 덩어리 카운팅한다
    # 이미 방문체크된것들은 한덩어리고 또 방문안된것을 탐색하게된다면 덩어리 하나가 더있다는 뜻이다
    return 1
while True:
    # 매해가 지날때마다 빙산이 녹거나 녹지않든 리셋팅을 해주어야 계산할 수 잇다
    visited = [[False]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            # 한번탐색하면 이어지는 노드들을 전부 방문체크해준다
            # 즉 결과리스트가 2개이상이되면 분리되었다고 판단한다
            if graph[i][j] != 0 and visited[i][j] == False:
                result.append(bfs(i,j))
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                graph[i][j] -= count[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0
    if len(result) > 1:
        check = True
        break
    if len(result) == 0:
        break
    day += 1
if check:
    print(day)
else:
    print(0)