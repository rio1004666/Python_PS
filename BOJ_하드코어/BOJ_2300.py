from math import inf

N = int(input())
gigi = []
for _ in range(N):
    a, b = map(int, input().split())
    gigi.append((a, abs(b)))
gigi.sort()

dp = [inf] * (N + 1) # DP라고해서 2중 FOR문을 안돌리진 않는다 하지만 시간초과 나는 경우가 컴파일러때문에 생긴다

dp[0] = 0 # 0번 인덱스는 첫번째원소가 아니다
dp[1] = gigi[0][1] * 2 # 첫번째 원소는 자기 자식 y좌표의 2배이다 => 처음이라도 포함시키려면 정사각형을 만들어야하므로 비용이 들어간다 높이 X 2 만큼 정사각형을 만들어줘야한다
# 그림을 그려가면서 어떻게 포함시키는정사각형태가 되게하고 분할하게 하는것이 좋은지 아니면 전부 포함시키는것이 좋은지 경우의 수중 최솟값을 선택해야한다
for i in range(2, N + 1): # 두번째원소부터 N번째원소까지 반복한다
    max_h = gigi[i - 1][1] # 우선 최고높이는 이전 원소의 높이라고 가정한다
    for j in range(i - 1, -1, -1): # 이전의 원소부터 하나씩 체크해본다
        max_h = max(max_h, abs(gigi[j][1])) # 최대높이는 계속 내려가면서 갱신시킨다
        # 인덱스가 헷갈리지만 DP테이블의 인덱스는 1번부터이고 DP[2]는 2번째 좌표까지 최소통신폭을 메모이제이션한것이고,
        # 그 이후 구간의 최소통신폭은 나머지점들의 최대높이와 X좌표 최대최소의 차이중 최댓값을 선택해야한다 => 그래야 문제조건에 충족시키는 포함한다를 만족한다
        dp[i] = min(dp[i], dp[j] + max(2 * max_h, gigi[i - 1][0] - gigi[j][0]))

print(dp[N])
total = 0
for i in range(1,10001):
    total += i
print(total)
