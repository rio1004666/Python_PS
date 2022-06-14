import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
# 1. 첫 번째 풀이 => 시간: O(N^2), 공간: O(N)
swap_cnt = [0 for _ in range(n)]
for i in range(n):
    # i 번지부터 존재하는 가장 작은 값과 그 위치를 찾는다.
    minValue, minIdx = a[i], i
    for j in range(i + 1, n):
        if a[j] < minValue:
            minValue, minIdx = a[j], j
    # swap 해주고 정답 기록하기
    if i != minIdx:
        a[i], a[minIdx] = a[minIdx], a[i]
        swap_cnt[i] += 1
        swap_cnt[minIdx] += 1
print(*swap_cnt)