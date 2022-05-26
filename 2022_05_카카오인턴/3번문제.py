# 1번작업 : A를 1증가시키는데 1시간
# 2번작업 : B를 1증가시키는데 1시간
# 3번작업 : 아이템을 써서 Ra (아이템을 쓰기위한 최소요건) ,Ca (T만큼의 시간을 들여서 증가가능), Rb (아이템을 쓰기위한 최소요건)  , Cb (T만큼의 시간을 들여서 증가가능), T
# 3번작업에서 아이템을 여러번쓸수잇다
# 최소시간에  Sa 가 Ga보다 크거나 같길바라고 Sb 가 Gb보다 크거나 같길 바람
# 그래프 문제 => 정점과 간선을 정의해서 요구하는 정답을 그래프로 잘 표현하기 즉 상태의 변화
# 혹은 다이나믹 프로그래밍 => dp 인덱스 => [1번작업][2번작업][3번작업] => 완전탐색에서 모든 경우의 탐색이 아니라
# 잘보면 어떻게 잘해서 A가 20이되고 B가 30이되면 시작하는 순간부터 그 중간과정을 모두 기억할 필요가 없다
# 걸리는 시간만 기억하면 된다 어떤 방법은 5시간 혹은 10시간 => 최단시간만 기억한다
# 즉 A값, B값 , Sa,Sb 가 A,B 까지 가는데 걸리는 최소시간
# 즉 3개의 값을 DP테이블에 넣어준다 DP[A][B] = T
# 각 A, B 까지 가는데 걸리는 시간이 T만큼 걸리더라
# 점화식 DP[A][B] =
# 첫번째 파티션  = 1번작업 => DP[A-1][B] => A에 1시간을 더하면  A와 B가 되므로 그전의 값인 A-1을 이용
# 두번째 파티션 = 2번 작업 => DP[A][B-1]
# 세번째 파티션 = 3번작업  => A-Ca,B-Cb => 무조건 아이템을 쓸수는 없고 각각 >=Ra 과 >=Rb를 만족해야 값을 가질수있다
import sys

MAX = 1000000000
si = sys.stdin.readline
SA, SB = map(int, si().split())
GA, GB = 0, 0
N = int(si())
items = [list(map(int, si().split())) for _ in range(N)]
for RA, RB, _, _, _ in items:
    GA = max(GA, RA)
    GB = max(GB, RB)
dy = [[MAX for _ in range(200)] for __ in range(200)]
dy[SA][SB] = 0


def renew(nextA, nextB, newValue):
    # dy[nextA][nextB] 를 newValue 로 갱신시켜라
    nextA = min(nextA, GA)
    nextB = min(nextB, GB)
    dy[nextA][nextB] = min(dy[nextA][nextB], newValue)


ans = MAX
for A in range(GA + 1):
    for B in range(GB + 1):
        # 현재 능력치가 A, B 이다.
        if dy[A][B] == MAX:
            # 도달할 수 없는 불가능한 상황
            continue

        # dy[A][B] 값을 알고 있다 == 시작 상황에서 A, B 까지 필요한 최소 시간을 안다.

        # 1. 이 순간에 1번 작업을 했을 때
        renew(A + 1, B, dy[A][B] + 1)
        # 2. 이 순간에 2번 작업을 했을 때
        renew(A, B + 1, dy[A][B] + 1)
        # 3. 이 순간에 아이템을 썼을 때
        for RA, RB, CA, CB, T in items:
            if A < RA or B < RB:
                continue
            nextA, nextB = A + CA, B + CB
            renew(nextA, nextB, dy[A][B] + T)
print(dy[GA][GB])