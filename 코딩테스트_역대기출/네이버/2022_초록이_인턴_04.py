# 지렁이 1살,2살,3살짜리가있다
# 지렁이 1살은 한칸 2살은 2칸 3살은 3칸이다 => 연속되어 있지만 일직선보장은없다
# 어떤 칸을 정했을 때 지렁이가 있다면 인접한 두칸에 지렁이가 있다면
# 얘는 3살일 수 밖에 없다
# 1살도 아니고 3살도 아니면 2살이다
# 그리고 인접한 지렁이 칸은 다를 수가없다 즉 같다

import sys

si = sys.stdin.readline
n, m = map(int, si().split())
a = [list(si().strip()) for _ in range(n)]
ans = [0, 0, 0] # 지렁이 마리수 세기 위한 배열 저장소


def in_range(i, j):
    return 0 <= i < n and 0 <= j < m


dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(n):
    for j in range(m):
        if a[i][j] != 'O': continue
        cnt = 0
        for di, dj in dir: # 인접한 칸을 체크
            ni, nj = i + di, j + dj
            if not in_range(ni, nj):
                continue
            if a[ni][nj] == 'O': # 지렁이칸이라면 갯수를 카운팅
                cnt += 1
        if cnt == 0:  # 1 year old => 1살짜리라면 1살짜리 지렁이 저장소에 차곡차곡 저장
            ans[0] += 1
            a[i][j] = 'X' # 빈칸으로 셋팅

        elif cnt == 2:  # 3 years old => 3살짜리라면 3살짜리 지렁이 저장소에 차곡차곡 저장
            ans[2] += 1
            for di, dj in dir: # 4방향돌리면서 지렁이인칸은 빈칸으로 셋팅
                ni, nj = i + di, j + dj
                if not in_range(ni, nj):
                    continue
                a[ni][nj] = 'X'
            a[i][j] = 'X' # 자기 자신칸도 빈칸으로 셋팅
for i in range(n):
    for j in range(m):
        if a[i][j] == 'O':  # one of 2 years old => 나머지는 2살짜리 지렁이이다
            ans[1] += 1
ans[1] //= 2 # 최종적으로 2칸짜리 지렁이는 칸수 자체를 2칸씩 세었기때문에 나누기 2로 해서 1마리로 친다
print(*ans) # 포인터로 배열을 가리킴