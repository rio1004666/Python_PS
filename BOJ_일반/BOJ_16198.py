# 분할정복으로 재귀함수를 수행시켜서 마지막 갯수가 3개인경우 리턴되면서 최종적으로 계산한다
# 제거된 구슬 기준으로 왼쪽 오른쪽리스트를 합쳐가면서 재귀적으로 반복시킨다
# 최종적으로 각 원소를 제거했을 경우 최댓갑시 남게 된다

import sys

input = sys.stdin.readline
N = int(input())
li = list(map(int, input().split()))
visited = [False] * N
visited[0] = True
visited[-1] = True
ans = list(li)
ret = 0


def func(sum, x):
    global ret
    if all(visited):
        ret = max(ret, sum)
        return
    for i in range(1, N):
        if not visited[i]:
            visited[i] = True
            x[i] = -1
            left = 0
            right = 0
            for j in range(i - 1, -1, -1):
                if x[j] != -1:
                    left = x[j]
                    break
            for k in range(i + 1, N):
                if x[k] != -1:
                    right = x[k]
                    break
            tmp = left * right
            sum += tmp
            func(sum, x)
            sum -= tmp
            x[i] = li[i]
            visited[i] = False


func(0, ans)
print(ret)