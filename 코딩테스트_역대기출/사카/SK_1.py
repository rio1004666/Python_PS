def solution(money, costs):
    answer = 0
    coins = [1, 5, 10, 50, 100, 500]
    cost500 = [costs[0] * 500, costs[1] * 100, costs[2] * 50, costs[3] * 10, costs[4] * 5,
               costs[5]]  # 500원보다 클때 // 500원 만드는데 필요한비용

    # 여기서 가장 작은게 만드는데 가장 적게들어가는 비용

    print(cost500)

    cost100 = [costs[0] * 500, costs[1] * 100, costs[2] * 50, costs[3] * 10, costs[4] * 5]  # 100원보다 클때
    cost50 = [costs[0] * 500, costs[1] * 100, costs[2] * 50, costs[3] * 10]  # 50원보다클때
    cost10 = [costs[0] * 500, costs[1] * 100, costs[2] * 50]  # 10원보다클떄
    cost5 = [costs[0] * 500, costs[1] * 100]  # 5원보다클때

    if money >= 500:
        answer += (money // coins[cost500.index(min(cost500))]) * costs[cost500.index(min(cost500))]
        # money  // (제일싼코인)500    * (비용)600
        money = money - (money // coins[cost500.index(min(cost500))] * coins[cost500.index(min(cost500))])

    if money >= 100:
        answer += (money // coins[cost100.index(min(cost100))]) * costs[cost100.index(min(cost100))]

        money = money - (money // coins[cost100.index(min(cost100))] * coins[cost100.index(min(cost100))])

    if money >= 50:
        answer += (money // coins[cost50.index(min(cost50))]) * costs[cost50.index(min(cost50))]
        money = money - (money // coins[cost50.index(min(cost50))] * coins[cost50.index(min(cost50))])

    if money >= 10:
        answer += (money // coins[cost10.index(min(cost10))]) * costs[cost10.index(min(cost10))]
        money = money - (money // coins[cost10.index(min(cost10))] * coins[cost10.index(min(cost10))])

    if money >= 5:
        answer += (money // coins[cost5.index(min(cost5))]) * costs[cost5.index(min(cost5))]
        money = money - (money // coins[cost5.index(min(cost5))] * coins[cost5.index(min(cost5))])

    if money > 1:
        answer += costs[0] * money

    return answer


money = 4578
costs = [1, 4, 99, 35, 50, 1000]
solution(money, costs)