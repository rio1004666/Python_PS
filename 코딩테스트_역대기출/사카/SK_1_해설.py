# 흔한 문제는 기본적인 코드가 필요하다
import sys
si = sys.stdin.readline
W = int(si())
weights = [1,5,10,50,100,500]
costs = list(map(int, si().split()))
dp = [[0 for _ in range(W+1)] for __ in range(6)]
for i in range(W+1):
    dp[0][i] = costs[0] * i
# 점화식

for k in range(1,6):
    for w in range(1, W+1):
        dp[k][w] = dp[k-1][w]
        if w - weights[k] >= 0:
            dp[k][w] = min(dp[k-1][w], dp[k][w-weights[k]] + costs[k])
print(dp[5][W])