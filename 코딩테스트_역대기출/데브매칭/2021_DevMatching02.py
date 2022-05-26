import sys
from collections import defaultdict

si = sys.stdin.readline()
n = int(si())
n, menu_cnt , order_cnt = map(int,si().split())
menu_map = dict()
for _ in range(menu_cnt):
    name, time = si().split()
    time = int(time)
    menu_map[name] = time # set

stove = [0] * n
ans = 0
for rep in range(order_cnt):
    name, order_time = si().split()
    order_time = int(order_time)
    # 1. 빈 화구 있니?
    flag = False
    for i in range(0,n):
        if stove[i] <= order_time: # 빈화구 찾음
            flag = True
            stove[i] = order_time + menu_map[name]
            ans = stove[i]
            break
    # 2. 빈 화구 없음 !
    if not flag:
        min_time = min(stove)
        for i in range(0,n):
            if stove[i] == min_time:
                stove[i] = stove[i] + menu_map[name]
                break
    if rep == order_cnt - 1:
        print(ans)