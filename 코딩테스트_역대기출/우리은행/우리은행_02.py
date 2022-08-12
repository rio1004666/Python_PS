# 2차원 격자 배열
# . 과 # 으로 이루어진 격자
#   # 이 도형을 형성해서 그 도현의 선과 내부 칸의 총 갯수
# 가장 자리에서 바다를 찾고 시작점으로 인접해있는 바다를 모두 찾는다
# 그 후 남은 물들이 호수이다 왜냐 경계선은 이미 테두리를 체크해 놓은 상태이다
# 주어진 지도를 확장해서 매딩한다
# 그 후에 패딩된 칸들을 체크하면 모든 바다를 한번에 탐색 가능하다
# 물론 모든 바다를 다 찾아서 체크해도 되지만...
# 그다음 전체 넓이에서 바다넓이를 빼면된다 
# 반대로 생각하기
import sys


import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = [['.'] * (m + 2)]
a += [['.'] + list(si().strip()) + ['.'] for _ in range(n)]
a += [['.'] * (m + 2)]
from pprint import pprint
pprint(a)


n += 2
m += 2
total_area = n * m
visit = [[0 for _ in range(m)] for __ in range(n)]
# bfs사용해도 됨
def dfs(x, y):
    global total_area
    visit[x][y] = 1
    total_area -= 1
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0 and a[nx][ny] == '.':
            dfs(nx, ny)
dfs(0, 0)
print(total_area)
