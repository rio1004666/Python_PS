1.
import sys
si = sys.stdin.readline
N, X = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(N)]
a.sort(key=lambda x: (x[0], -x[1]))
ans = 0
for _, cnt in a:
    if cnt <= X:
        X -= cnt  # 남은 물건 줄이기
        ans += cnt  # 판매 개수 누적
print(ans)
# 5 20
# 3 20
# 1 1
# 4 7
# 1 4
# 3 5
# => 17
