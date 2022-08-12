# 2차원 격자
# 바깥에 화살표방향으로 민다 ( 번호가 순서대로 0,0위치부터 옆으로 매겨짐 )
# 이 화살표 방향으로 밀면 한칸씩 밀어짐 즉 한 열 혹은 한 행 밀어버림
# 끝에 더이상 밀리지 않으면 가만히 있게 됨
# 또 특이하게 T라는 값이 주어지면
# 어떤 공이 더이상 격자 밖으로 움직이지 못하는 상황이면
# T가 2라면 마지막 걸쳐있는 공이 T개 이상 공들에 의해서 밀린다면
# 격자 밖으로 사라짐 ( 자기 자신 제외 )
# 단순 시뮬레이션
# 우선 번호와 방향을 기록해야한다
# 각 쿼리 번호마다 밀어버리는 동작을 하는 함수를 구현
# N과 T느 10이하이다 => 시간복잡도 그렇게 많지 않을것이다
# 쿼리 횟수도 많아야 100개 추측
# 구현 모델링
# 시계방향으로 번호가 매겨지는 것
# 몇번이 어떤 행이나 열을 어느 방향으로 밀어버리는지를 찾아야함
import sys

si = sys.stdin.readline
N, Q, T = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(N)]


def push(num):
    if num <= N:  # upper side
        col = num - 1

        # drop check
        cnt = 0
        for row in range(N - 2, -1, -1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:  # drop the last ball
            a[N - 1][col] = 0

        # push one step
        for row in range(N - 1, 0, -1):
            if a[row][col] == 1: continue
            a[row][col], a[row - 1][col] = a[row - 1][col], a[row][col]
    elif num <= N * 2:  # right side
        row = num - N - 1
        # drop check
        cnt = 0
        for col in range(1, N, 1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:
            a[row][0] = 0

        # push one step
        for col in range(0, N - 1):
            if a[row][col] == 1: continue
            a[row][col], a[row][col + 1] = a[row][col + 1], a[row][col]

    elif num <= N * 3:  # lower side
        col = N - (num - N * 2)

        # drop check
        cnt = 0
        for row in range(1, N, 1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:  # drop the last ball
            a[0][col] = 0

        # push one step
        for row in range(0, N - 1, 1):
            if a[row][col] == 1: continue
            a[row][col], a[row + 1][col] = a[row + 1][col], a[row][col]
    else:  # left side
        row = N - (num - N * 3)
        # drop check
        cnt = 0
        for col in range(N - 2, -1, -1):
            if a[row][col] == 0: break
            cnt += 1
        if cnt >= T:
            a[row][N - 1] = 0

        # push one step
        for col in range(N - 1, 0, -1):
            if a[row][col] == 1: continue
            a[row][col], a[row][col - 1] = a[row][col - 1], a[row][col]


for _ in range(Q):
    num = int(si())
    push(num)
for i in range(N):
    print(*a[i])