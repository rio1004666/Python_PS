# 2차원 배열이 주어짐
# 6각형 배열로 바뀐다
# 좌표가 주어져서 이으면 단순 다각형이 만들어진다
# 지나간 칸들을 색칠한다
# 색칠되어 있는 인접한 칸들을 찾는다
# 그것을 원래 배열에서 찾는다
# 그 숫자들의 합을 찾는다 ...=> 구현 시뮬레이션 그냥 하면된다
# 6각형에서 방향이 6가지 방향이므로 그렇게 방향을 저장한다
# 6방향으로 가면 어떻게 좌표가 바뀌는지...
# 이쁘게 4방향으로 맞아 떨어지지 않음
# 오른쪽 위 방향은 +0,+1 이되는데
# 2,2 에서 오른쪽 위 방향은 -1,+1 방향이 된다.... 변화량이 다른게 문제다
# 아 주  귀 찮 은 문 제 다
# 방향별로 번호를 매길것이다
# 위쪽 방향 0 오른쪽위 1 오른쪽 아래 2....이런식으로 번호를 매기고
# 이럴때도 규칙성을 찾아야할듯....
# 0번방향과 3번방향은 위아래이므로 항상 변화량이 같다
# 1번방향으로 가게 되면 열번호에 따라 달라짐!!!!!!!!!!!!!! 즉 열번호가 홀수냐 짝수냐!!!
# 이 규칙을 찾으면 쉬워짐.....변화량이 홀수냐 |짝수냐 구분만 해주면 되기 때문에
# 이 테크닉은 정말 자주 쓰이는 테크닉이므로 기억해 둔다....나도 가끔씩 까먹는다
# 예를들어서 1,0 에서 2,3으로 가고싶다 시작점과 도착점만 가지고는 어떤 방향으로 가야하는지 알 수 없다
# 이 문제에서 행과 열의 길이가 10밖에 안되므로 수학을 모르더라도 방향을 알 수 있다
# 맵을 벗어 날때까지 찾지 못하면 다른 방향으로 선택한다 모든 방향으로 쭉가본다
# 즉 여기서 방향을 하나 정해놓고 도착점을 만나면 d = 2로 결정한다
# 중간에 이동이 휘어지는 경우는 없으므로 가능한것이다
# 맵의 크기도 작다
# 그리고 색칠까지 다하고 그 이후에 인접한 모든 칸에 색칠 한다
# 모든 칸을 순회하면서  (브루트 포스) 그 위치의 숫자를 정답에 추가한다
# 근데 방향설정은 모든 칸을 끝까지 안가보고도 알 수 있다
# 방향으로 끝까지 쭉 가는 경우라면 변화량은 일정하기에
# 한 꼭지점과 한 꼭지점의  변화량을 계산해주면 방향이 나올것이다
# 아니다 그러면 모든 방향을 또 체크해야하므로 모든 방향에 끝까지 가보는것이 나을지도 모른다


import sys

si = sys.stdin.readline

# 입력부분 (생략 )
n, m = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(n)]
visit = [[0 for _ in range(m)] for __ in range(n)]

# 하드 코딩
# 6각형 칸의 방향을 결정후 이동
# 각 방향이 홀수와 짝수로 나누는 특수한 경우이므로
# 그 좌표와 방향을 입력받아 다음 칸을 이동하는 함수를 정의함
# 여기서 x는 행 y는 열을 설정함
def move(x, y, d):
    if d == 0: return (x - 1, y)
    if d == 1:
        if y % 2 == 0:
            return (x - 1, y + 1)
        else:
            return (x, y + 1)
    if d == 2:
        if y % 2 == 0:
            return (x, y + 1)
        else:
            return (x + 1, y + 1)
    if d == 3: return (x + 1, y)
    if d == 4:
        if y % 2 == 0:
            return (x, y - 1)
        else:
            return (x + 1, y - 1)
    if d == 5:
        if y % 2 == 0:
            return (x - 1, y - 1)
        else:
            return (x, y - 1)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 색칠된 칸에서 부터 모든 방향을 가보면서 전부 끝까지 가보고 도착점을 만나면 색칠을 멈춘다
# visited 는 색칠한는 2차원 방문 리스트이다
def coloring(start, goal):
    for d in range(6):
        flag = False
        p = start
        # 이 반복문은 모든 방향에 쭉 탐색해보는 것이다 목표점이 있는지
        while in_range(p[0], p[1]):
            p = move(p[0], p[1], d)
            if p == goal:
                flag = True
                break
        # 한 방향으로 쭉가다가 목표도착했다면
        # 그 방향으로 목표까지 쭉 색칠하는 과정이다
        if flag:
            p = start
            while p != goal:
                p = move(p[0], p[1], d)
                visit[p[0]][p[1]] = 1
            break



cnt = int(si())
points = [tuple(map(int, si().split())) for _ in range(cnt)]
points.append(points[0])


for i in range(cnt):
    cur = points[i]
    nxt = points[i + 1]
    # 지금 꼭지점에서 다음 꼭지점까지 색칠을 해줄 것이다
    coloring(cur, nxt)
ans = 0
# 모든 격자를 보면서 6방향중에서 색칠된것이 하나라도 있따면
# 좌표값의 숫자를 정답에 추가한다
for i in range(n):
    for j in range(m):
        if visit[i][j] == 1: continue
        flag = 0
        # 모든 방향을 확인 하나라도 색칠해있다면 정답에 추가
        # 그러기 위해서 플래그 변수 설정 하므로서 체크함
        for d in range(6):
            ni, nj = move(i, j, d)
            if in_range(ni, nj) and visit[ni][nj] == 1: flag = 1
        if flag == 1:
            ans += a[i][j]

print(ans)