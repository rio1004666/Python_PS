# 주식 N개의 상품 존재 20 이하
# 각 상품별로 최소 투자 금액 과 최대 투자 금액 과 이익률을 알고 있음
# 최소 투자금액은 이 상품을 선택했을 경우 "무조건" 사야함
# 최대 투자금액은 범위상 최대한도로 살 수 있다는 것을 의미
# 그래서 여기서 무조건이라는 키워드가 등장하므로 브루트 포스로 다 사보면서 무조건 사고 남은 금액으로 그리디하게 투자하면 된다
# 전체 돈이 무한대가 아니다
# 20개의 상품중에서 얼마씩을 넣어야 돈을 제일 많이 벌 수 있을까
# 우선 20개의 상품뿐이다 그러면 브루트 포스 생각
# 브루트 포스 중에서 조합 순열 백트래킹 다양하게 있는데
# 돈을 많이 벌 수 있다는 말은 최대값이란 것이고
# 그리고 정렬이 필요하다 최대투자금액으로  => 그리디하게 구하는 값이 최선의 결과를 나으므로
# 모든 상품중에 돈을 다사용해서 최대로 몇개의 투자 상품을 고를 것이고
# 그로 얻는 수익을 플러스해서 최대로 돈을 많이 벌 수 있는 값을 얻데이트 하는 것이므로
# 브루트 포스로 백트래킹을 사용하면 된다
# 여기서 백트래킹을 사용하려면 재귀함수가 필요하다 깊이로 들어가
# 다시 나와서
# 1번 상품 최소 1000 최대 3000 이익률 70%
# 2번 상품 최소 8000 최대 10000 이익률 60%
# 3번 상품 최소 5000 최대 8000 이익률 55%
# 내가 가진 10000원을 어떻게 분배해야 최대 이익을 낼 수 있을 까?
# 어떻게 분배해야 에서 키워드가 잡힌다 즉 이것저것 모든 상품에 다 분배해서 투자해보고 그중에서 최대 이익을 낼 수 있으므로
# 1번 상품과 3번 상품에 3000원과 7000원을 투자하고 2번은 포기함
# 3000 x 0.7 + 7000 x 0.55 = 3850 + 2100 = 5950
# 또 다른 예로 1번상품과 2번상품에 각각 2000과 8000을 투자하면 1번과 3번보다 더 많은 이익을 얻음
# N = 20
# 최소치가 존재한다..투자마다
# 만약 최소치가 존재하지 않는다면 그리디하게 큰 수익률부터 계산하면되지만
# 최소치가 존재한다면 어려워진다
# 정답 투자가 존재한다 => 어디에 투자했는지 모른다
# 생각의 전환 필요하다
# 세개의 종목을 바로 찾으려고 하지 않고
# 투자할 종목을 결정하고 완전탐색한다
# 1번만 투자햇을때 최대 이익
# 2번만 투자했을 때 최대 이익
# 3번만 투자했을 때 최대이익
# 2,4 ,5 에 투자했을 때 최대 이익
# 1,2,3,4,5 에 투자했을 때 최대 이익
# 즉 전부 다 결정하고 최대이익을 계산한다
# 이러한 방법이 가능한 이유는 N이 20이라서
# 이 문제에서 핵심 관철은 N = 20이라는 것
# 그리고 최소로 사야하는 값이 존재한다는것
# 최종적으로 무엇을 사야 최대가 될지 모르기때문에 미리 정답을 구해놓고
# 정답을 업데이트 할 수 있다는것
# 정답을 미리 구했다는 것은 무조건 최소로 일단 사고 나서
# 남은 최대치로 이익률이 최대로 계산된 값들을 정답에 업데이트 하면된다는것
import sys

si = sys.stdin.readline
N, Money = map(int, si().split())
items = [tuple(map(int, si().split())) for _ in range(N)]

# 왜 이익률기준으로 내림차순 정렬해서 그리디하게 이익률 큰것인 상품부터 투자하는지 알겠다
# 내가 가진 돈의 한도가 없다면 금액과 이익률 모두 고려해야하지만
# 한도가 존재하기때문에 내가 살수있는 금액은 정해져잇으므로 이익률 이 큰것부터 투자해야한다

items.sort(key=lambda x: -x[2])
selected = []
ans = 0


def solve():
    global ans, Money
    money = Money # 매번 돈을 초기화 해야함
    interest = 0 # 매번 이자액을 계산해야 함 => 초기화 해야함
    # 여기서 각 상품을 골라서 적절히 투자해서 최대치를 얻고
    # 어떻게 최대이익을 구해???? 를 해결해야한다
    # 일단 예를 들어 4, 8, 13의 투자 상품을 골랐고 무조건 사야한다
    # 4 상품이 최소 10만 최대 100만 이익률 40% - 최소치 사고 90만 남음 => 36만원 수익
    # 8 상품이 최소 30만 최대 90만 이익률 80% - 최소치 사고 60만 남음 => 48만원 수익
    # 13 상품이 최소 20만 최대 120만 이익률 35% - 최소치 사고 100만 남음 => 35만원 수익
    # 위의 경우에서 이익률이 최대인것이 최대의 수익을 얻으므로 이익률 순으로 정렬했던 것이다 위에서
    # 모든 상품의 최소치를 전부 무조건 사본다
    # 근데 궁금한것은 이익률이 최대라고 해서 꼭 최대 이익을 얻는것은 아닌것같다 ..... 60만원의 수익률이 50프로라면 가장 최대이지만 수익이 제일 적게 난다

    # 무조건 사야하니까...
    # 그리고 이제 최소는 0으로 바뀐다 왜냐면 4상품에서 10만을 삿고
    # 원래 최대가 100만이므로 90만을 더 살 수 있기 때문이다
    # 나머지도 마찬가지이다
    # 그래서 모든 종목들에 대해 최소치를 우선 사고 ( 최소치는 최소 꼭 구매해야 하는 금액이기때문 )
    # 지금 고른 종목들은 머살지 결정을 했기 때문에 무조건 3상품은 전부 사야한다
    # 이러한 관찰이 필요하다 그리디하게
    # 이제 남은돈으로 마음대로 고를 수 있다
    # 이 상황에서 최소는 구애 받지 않은 상태가 되고
    # 최대치와 이익만 남았기때문에 여기서 그리디하게 풀면된다
    # 남아 있는 돈이 없다면 즉 마이너스라면 불가능하므로 정답을 구할 수 없게되고
    # 가장 이익이 많이 나올 수 있는 돈부터 구하면된다
    # 각 상품들의 이익을 전부 구하면서 투자한다
    for idx in selected:
        money -= items[idx][0]  # minimum invest
        interest += items[idx][0] // 100 * items[idx][2]

    if money < 0:  # Impossible choice
        return

    for idx in selected:
        invest = min(money, items[idx][1] - items[idx][0])
        money -= invest
        interest += invest // 100 * items[idx][2]
    # 최종 최댓값 업데이트를 친다
    ans = max(ans, interest)


def backtracking(idx):
    if idx == N:
        solve()
        return
    # 2^N 가지에 대해 모든 최대 이익을 구할 것이다
    # 2^20은 그렇게 큰 경우의 수가 아니다
    selected.append(idx)
    backtracking(idx + 1)
    selected.pop()
    backtracking(idx + 1)


backtracking(0)
print(ans)
