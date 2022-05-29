# 이분탐색
# 역발상으로 구하기
# 구하기가 힘들다고 생각되면 
import sys
from math import ceil, sqrt
si = sys.stdin.readline
n, total_fuel = map(int, si().split())
powers = list(map(int, si().split()))
distances = list(map(int, si().split()))
L = 0
for i in range(n):
    p = powers[i]
    dist = distances[i]
    # 0.5 * p * T^2 = dist
    # T = sqrt(2 * dist / p)
    T = ceil(sqrt(2.0 * dist / p))  # 이 차가 최소한으로 필요한 시간
    L = max(L, T)
def check(T):  # T 초 만에 모든 자동차가 갈 건데, 이때 연료량이 fuel_total을 넘지 않는가?
    fuels = 0
    for i in range(n):
        p = powers[i]
        dist = distances[i]
        f = ceil(T - sqrt(p * p * T * T - 2 * dist * p) / p)  # 이 차가 필요로 하는 연료 량
        fuels += f
    return fuels <= total_fuel
R = 2000000
ans = 0
while L <= R:
    mid = (L + R) // 2
    if check(mid):
        ans = mid
        R = mid - 1
    else:
        L = mid + 1
print(ans)