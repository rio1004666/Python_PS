import sys
si = sys.stdin.readline
n = int(si())
a = list(map(int, si().split()))
# 선택정렬을 햇을 경우 각 위치의 숫자가 몇번 스왑됬는지 체크함
# 각각의 위치에서 스왑될때마다 카운팅을 기억해주는 배열을 만들어서 세어준다
# N제한 1000
# 1. 첫 번째 풀이 => 시간: O(N^2), 공간: O(N)
swap_cnt = [0 for _ in range(n)]
for i in range(n):
    # i 번지부터 존재하는 가장 작은 값과 그 위치를 찾는다.
    minValue, minIdx = a[i], i
    for j in range(i + 1, n):
        if a[j] < minValue:
            minValue, minIdx = a[j], j # 일단은 기억해둔다
    # swap 해주고 정답 기록하기
    if i != minIdx:
        a[i], a[minIdx] = a[minIdx], a[i]
        swap_cnt[i] += 1
        swap_cnt[minIdx] += 1
print(*swap_cnt) # C언어와 같다 배열을 출력할경우 포인터로 주소만 가져와주면 그 배열을 전부 출력한다

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
    # 매순간 정렬되는것을 기록한다
    path.append(copy.deepcopy(a))
swap_cnt = [0 for _ in range(n)]
for j in range(n):
    for i in range(1, n):
        # 그 전과 다르다면 스왑된것이므로 카운팅된다
        if path[i][j] != path[i - 1][j]:
            swap_cnt[j] += 1
print(*swap_cnt)