# 그래프 - 최소이동횟수에서 힌트얻음
# 상태의 변화가 그래프가 될 수 있음
# 왼쪽 출발지 상태 기록 => 늑대수 , 양수,  배추수 사람은 어딧느냐
# 전체의 늑대 양수 배추수 는 동일하기 떔분!
# 출발지만 알면 목적지는 자동으로 알게됨
# 상태를 하나의 정점으로 바라보다!!!!!
# Wn, Sn, Cn, Pn => 이게 다른 상태(정점)로 변화함
# 상태와 행동이 명확히 주어지면 최소 이동횟수를 구한다면 그래프문제로 생각해보자
# 간선의 정의는 어떤 상태에서 다른 상태로 배를 타고 건너서 변화할 수 잇는 상태
# 무엇이 좋을까?
# 늑대 5 양 6 배추 10 => (5,6,10,0) 초기상태
# A에서 B까지 최소갯수의 간선을 타고 갈수잇다면 그것이 정답
# 그래프에서 시작점과 목표지점이 정해졌을 때 최소횟수를 구하고싶으니까 bfs를 사용할 수 있다
# 물통이라는 문제와 비슷하다!!!!!!!!


import sys
from collections import deque

si = sys.stdin.readline
L = int(si())
numWolf, weightWolf = map(int, si().split())
numSheep, weightSheep = map(int, si().split())
numCabbage, weightCabbage = map(int, si().split())
dist = [
    [
        [
            [-1 for _ in range(2)]
            for __ in range(numCabbage + 1)
        ] for ___ in range(numSheep + 1)
    ] for ____ in range(numWolf + 1)
]
que = deque()
que.append((numWolf, numSheep, numCabbage, 0))
dist[numWolf][numSheep][numCabbage][0] = 0
while que:
    w, s, c, p = que.popleft()  # (w, s, c, p) 라는 정점에 도달한 상황

    if p == 0:
        personW, personS, personC = w, s, c
    else:
        personW, personS, personC = numWolf - w, numSheep - s, numCabbage - c  # 현재 사람 쪽에 있는 개체 수

    # 이 정점에 인접한 모든 간선을 보자!
    # 각 사람이 데려가는 늑대수, 양의수 , 배추수이다
    for boatW in range(personW + 1):
        for boatS in range(personS + 1):
            for boatC in range(personC + 1):
                # 1. 배에 다 탈 수 있어?
                totalWeight = boatW * weightWolf + boatS * weightSheep + boatC * weightCabbage
                if totalWeight > L:
                    continue

                # 2. 배 타고 넘어갔을 때 남아있는 애들이 안전해? => 반대쪽은 전체수-개체수
                if personW - boatW >= personS - boatS > 0:
                    continue
                if personS - boatS >= personC - boatC > 0:
                    continue

                # 3. 배 타고 넘어간 순간이 이미 방문한 적이 있는 상황이야?
                if p == 0:  # 배가 출발지->목적지 이동
                    # 태울수 잇는 각 개체수를 파악하여 새로운 상태로 간선을 타고 이동한다
                    nW, nS, nC, nP = w - boatW, s - boatS, c - boatC, 1
                else:  # 배가 목적지->출발지 이동
                    nW, nS, nC, nP = w + boatW, s + boatS, c + boatC, 0
                if dist[nW][nS][nC][nP] != -1: # 이미 방문했다면 최소이므로 제외한다(시간단축)
                    continue
                dist[nW][nS][nC][nP] = dist[w][s][c][p] + 1 # 현재 거리에서 그다음 상태로 가게되면 +1 거리를 카운팅해준다
                que.append((nW, nS, nC, nP))
print(dist[0][0][0][1])