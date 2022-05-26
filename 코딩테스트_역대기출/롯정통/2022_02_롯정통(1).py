# 물건이 X개 있고 사람이 N명 있다
# N명은 각각 Level이랑 구매하고 싶은 물건의 갯수가 주어짐
# 하고싶은건 Level이 낮은사람이 먼저 구매
# 만약 남은 물건보다 많이 사고 싶으면 구매불가 => 다음 사람이 구매시도
# X개중에 몇개나 팔렸을까라는 것
import sys
si = sys.stdin.readline
N, X = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(N)]
a.sort(key=lambda x: (x[0], -x[1])) # 레벨순으로 정렬하고 그다음 가장 많이 사고자하는 물건순으로 정렬
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
