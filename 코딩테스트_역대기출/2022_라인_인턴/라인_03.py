# 이분탐색 => 브루트포스로 불가
# 역발상으로 구하기 => 연료를 구하기 힘들면 시간!!!을 찾아서 연료가 되는지 확인한다
# 구하기가 힘들다고 생각되면
# 이분탐색 문제는 정렬되어 있고 선형자료구조에서 값을 찾기 위한 최적의 알고리즘이다
# 연료를 적절히 배분하는 것이 아닌 시간을 딱 정해놓고 연료계산을 해서 총합보다 작은지 판단
# 이와 관련된 백준문제가 많다


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
    if check(mid): # 모든 자동차가 T시간내에 연료를 합해보니 가능하면 R을 땡긴다 시간을 줄여본다
        ans = mid
        R = mid - 1
    else: # 가능하지 않으면 시간을 늘려본다
        L = mid + 1
print(ans)