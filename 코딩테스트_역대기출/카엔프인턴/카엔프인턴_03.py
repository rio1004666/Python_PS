import sys
from itertools import permutations
import copy
# sys.setrecursionlimit(10000)
# si = sys.stdin.readline
#
# N = int(si())
#
# type = [1,2,4,6]
# answer = 0
# def DFS(cnt, total, arr):
#     global answer
#     if total == N:
#         # 굳이 순열 돌릴 필요가 없다
#         answer += 1
#         return
#     for i in range(4):
#         arr.append(type[i])
#         DFS(cnt + 1, total + type[i], arr)
#         arr.pop()
# for i in range(4):
#     DFS(1,type[i],[type[i]])
# print(answer%1000000007)
# 위는 시간초과
# from itertools import product
# # 2명이서 단쉬 4가지종류로 만들 수 있는 조합
# answer = 0
# for i in range(1,30):
#     for candi in product([1,2,4,6],repeat=i):
#         make = sum(candi)
#         if make == 29:
#             answer += 1
# print(answer)
#중복순열이나 dfs방식이나 그게그거다

# 위의 경우 브루트포스로 풀게되면 시간초과이다 4^3000 => DP 접근

# 모든 경우의 수를 기록하고 그 전의 기록을 이용한다!

# 점화식 dp[i][j] = i명이 j개의 가마니를 드는 방법의 수
import sys

si = sys.stdin.readline
N = int(si()) # 마을 사람 5명이 있고 5명이 5개의 가마니를 채워넣는 모든 경우의 수
# 우선 dp 배열을 생성해야한다
dp = [[0]*(3000+1) for _ in range(3000+1)] # 어차피 최대 3000개 제한이므로 900만 공간복잡도를 가지고 시간복잡도도 900만이다
# 우선 1명이 들 수 있는 모든 경우의 수는 초기화 될 수 있다 ( 0 개를 드는 것은 계산하지 않는다 )
dp[1][1] = 1 # (1)
dp[2][1] = 1
dp[3][1] = 1
dp[3][2] = 2

for i in range(2,3000+1):
    if i == 2 or i == 4 or i == 6:
        dp[i][i] += 1
    dp[i][i] += 1
# 3명까지는 명시적으로 개수가 몇개안되므로 초기화를 하고 4명이 드는 경우의 수부터 세야한다
for i in range(4,3000+1):
    for j in range(1,i):
        # i명이 i-1개를 드는 방법에서 추가적인 경우의 수가 발생하므로
        # 조건을 주어야한다
        if j !=  i - 1:
            dp[i][j] += dp[i-1][j] # 5명이 3개를 드는 경우와 4명이 3개를 드는 경우는 같다
        elif j == i - 1:
            dp[i][j] += dp[i-1][j] + (j-1)
answer = 0
for i in range(1,N+1):
    answer += dp[i][N]
print(answer)