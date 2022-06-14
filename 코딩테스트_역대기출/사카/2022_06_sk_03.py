import sys

si = sys.stdin.readline
n_topping, n_pizza, n_customer = map(int, si().split())
sizes = []  # 피자 번호 순 크기 배열
added_topping = [n_pizza for _ in range(n_topping + 1)]  # added_topping[i] := i번 토핑이 추가된 피자의 번호
for i in range(n_pizza):
    size, *toppings = map(int, si().split())
    sizes.append(size)
    for topping in toppings:
        added_topping[topping] = i  # topping이 i번 피자에서 처음 추가됐더라~


def get_size_number(size):
    if size > sizes[-1]:
        return n_pizza
    l, r, mid, ans = 0, n_pizza - 1, 0, n_pizza - 1
    while l <= r:
        mid = (l + r) // 2
        if sizes[mid] >= size:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans


def get_topping_number(toppings):
    ans = -1
    for topping in toppings:
        ans = max(ans, added_topping[topping])
    return ans


for i in range(n_customer):
    required_size, *required_toppings = map(int, si().split())
    # 1. required_size 를 만족하는 피자 번호의 최솟값
    size_number = get_size_number(required_size)
    # 2. required_toppings 를 만족하는 피자 번호의 최솟값
    topping_number = get_topping_number(required_toppings)

    ans = max(size_number, topping_number)
    if ans == n_pizza:
        ans = -1
    print(ans + 1)