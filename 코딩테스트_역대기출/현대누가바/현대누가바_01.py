# n=7
# 7개의 숫자
# 딱 한번만 숫자의 위치를 바꿔서 전체 숫자가 오름차순정렬이면
# yes 아니면 no
# 완전탐색 과 수학적 풀이
# 할 수 있는 행위  : 단 한번 두 원소의 위치를 바꿔봄
# O(N^2) * O(N) = O(N^3)
# 만약 N이 10만이면 정렬된것과 비교해서
# LIS 가 N-2라고 한다다
# 최장 오름차순 정렭된 갯수가 N-2개라면
# 2개만 정렬이 안됫다는 의미이므로
# 그렇게 비교하면서 풀면 좋다

import sys

si = sys.stdin.readline
N = int(si())
arr = list(map(int, si().split()))
result = sorted(arr)
cnt = 0
for i in range(N):
    if arr[i] != result[i]:
        cnt += 1
# 1자리가 다르다면 다른 자리도 분명 다를 것이다 => 1개의 원소가 정렬한 순서와 다르다면 그 원소 대신 다른 자리에 그 원소가 있다는 것이므로 반드시 두개가 다름을 보장한다
differ = N - cnt
if differ == N - 2:
    print("yes")
else:
    print("no")