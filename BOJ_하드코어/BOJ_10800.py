# 공번호 공색 공크기가 주어지면 각 공번호별 조건에 충족하는 공크기의합을 구하기

from collections import defaultdict
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ball = []
    for i in range(n):
        c, s = map(int, sys.stdin.readline().split())
        ball.append([c, s, i])

    # 공의 크기 순으로 정렬
    ball.sort(key=lambda x: x[1])

    answer = defaultdict(int)
    ball_size_sum = defaultdict(int)  # 색깔 별 공의 크기 누적합

    total = 0  # 총합
    i, j = 0, 0
    for i in range(n):
        while ball[j][1] < ball[i][1]:  # 크기가 작을 때까지 수행 # 이렇게 해야 같은 크기도 sum이 안쳐진다
            total += ball[j][1]
            ball_size_sum[ball[j][0]] += ball[j][1]
            j += 1
        answer[ball[i][2]] = total - ball_size_sum[ball[i][0]]  # 총합 - 현재 색깔 공 누적합

    for i in range(n):
        print(answer[i])