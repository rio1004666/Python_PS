from collections import defaultdict
coord = defaultdict(tuple)
def get_complexity(x, y):
    return abs(coord[x][0]-coord[y][0])+abs(coord[x][1]-coord[y][1])
def solution(X):

    MOD = 1000000007
    # 각 키보드문자들의 복잡도를 구하기위해 위치를 저장할것이다.
    # 키보드를 2차원배열형태로 저장한다.
    keyboard = ["qwertyuio", "pasdfghjk", "lzxcvbnm"]
    ans = 0
    # 각 문자에 대해 좌표를 저장한다.
    for i in range(3):
        for j in range(len(keyboard[i])):
            coord[keyboard[i][j]] = (i,j)

    N = len(X)
    for i in range(1, N):
        # 부분문자열에 대한 가능한 갯수를 구한다.
        cnt = i * (N - (i+1) + 1)
        cnt %= MOD
        # 연속한 두 문자열의 복잡도를 구한다.
        # abcc이면 bc부터 구한다.
        # abc / bc / bcc  / abcc

        C = get_complexity(X[i-1], X[i])

        ans += ((cnt*C) % MOD)
        ans %= MOD

    print(ans)

solution("abcc")