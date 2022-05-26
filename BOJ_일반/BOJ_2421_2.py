import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def recur(a, b):
    if a == 1 and b == 1:
        return 0
    if dp[a][b] != -1:
        return dp[a][b]

    case1 = case2 = 0
    # 현재 a수와 b수가 더해져서 소수냐 아니냐에 카운팅이 되냐 안되냐가 결정된다
    if is_prime[int(str(a) + str(b))]:
        if a > 1: case1 = recur(a - 1, b) + 1
        if b > 1: case2 = recur(a, b - 1) + 1
    else:
        if a > 1: case1 = recur(a - 1, b)
        if b > 1: case2 = recur(a, b - 1)

    dp[a][b] = max(case1, case2)
    return dp[a][b]


if __name__ == "__main__":
    N = int(input())

    # 소수 전처리
    is_prime = [True for _ in range(1000000)]
    for i in range(2, 1000000):
        for j in range(i + i, 1000000, i):
            if not is_prime[j]: continue

            is_prime[j] = False

    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    print(recur(N, N))