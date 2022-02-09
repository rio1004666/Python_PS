def solution(land):
    answer = 0

    n = len(land)

    dp = [[0] * 4 for col in range(n)]

    dp[0][0] = land[0][0]
    dp[0][1] = land[0][1]
    dp[0][2] = land[0][2]
    dp[0][3] = land[0][3]

    for cnt in range(1, n):
        for i in range(4):
            for j in range(4):
                if i == j: continue
                dp[cnt][i] = max(dp[cnt][i], dp[cnt - 1][j] + land[cnt][i])
    for i in range(4):
        answer = max(answer, dp[n - 1][i])
    return answer
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))