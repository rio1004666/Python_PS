# 2. 두 번째 풀이 => 시간: O(N^2), 공간: O(N^2)
import copy

path = [copy.deepcopy(a)]
for i in range(n):
    # i 번지부터 존재하는 가장 작은 값과 그 위치를 찾는다.
    minValue, minIdx = a[i], i
    for j in range(i + 1, n):
        if a[j] < minValue:
            minValue, minIdx = a[j], j
    # swap 해주고 정답 기록하기
    if i != minIdx:
        a[i], a[minIdx] = a[minIdx], a[i]

    path.append(copy.deepcopy(a))
swap_cnt = [0 for _ in range(n)]
for j in range(n):
    for i in range(1, n):
        if path[i][j] != path[i - 1][j]:
            swap_cnt[j] += 1
print(*swap_cnt)
