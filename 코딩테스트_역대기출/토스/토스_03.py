# 문자 기록 데이터베이스가 있다
# 이 데이터베이스는 각 문자가
# 누가 누구에게 문자를 언제 보냈느냐를 하나의 정보로 치면
# 이 정보의 리스트가 있다
# 0번사람이 3번 사람한테 문자를 보냄
# 문자 내용은 숫자로 표현됨 즉 34와 같이 보냄
# 언제 보냇냐 2022-08-10 04:28:52
# 이런 기록이 M개 있다
# 숫자는 0이상 N이하가 됨
# 각 사람마다 직접지인수와 간접지인수를 찾고 싶다
# 직접지인이란 A와 B가 같은 사람한테 동일한 문자를 10분이내로
# 보낸적이 있다면 A와 B는 직접지인이 된다
# 간접지인이란 A와 B가 동일한 다른 사람과 직접 지인관계면 된다
# 즉 A와 D가 직접지인 B와 D 직접지인이면 A와 B는 간접지인이 된다
# M은 1만개 N은 200이다
# 문자메시지 숫자의 크기는 1억
# 로그 기반의 그래프를 정의할 수 있다
# 정점과 간선을 정의할 수 있다
# 그래프 구성방법
# 정점은 자연스럽게 사람 한명이 하나의 정점이 됨
# 간선은 어떻게 정의되는것인가
# U <-> V : U번사람과 V번사람이 직접지인일때 직접지인일때 연결해줄것이다
# 로그를 기반으로 직접지인인지 판단 할 수 있다
# 모든 로그들을 즉 M개의 로그중 2개 선택해서
# 두 로그가 같은 사람에게 가는 문자고
# 같은 문자내용을 담고 있고
# 두시간차이가 10분이내라면
# 직접지인이라고 판단하고 간선을 이어준다
# pair 방식 => N^2이 됨
# 1억이 되지 않나 => 어쩔수업는듯 다른방법이 없다
# 직접지인수와 간접지인수 구하기
# 정점에 연결되어 있는 간선의 갯수 즉 차수가 직접지인수가 된다
# 간접지인수는 간선을 두개타서 도착할 수 있는 정점이 간접지인이 된다
# BFS사용해서 거리 2인 정점을 구할 수 있다

import sys
from datetime import datetime
from collections import deque
si = sys.stdin.readline
N, M = map(int, si().split())
logs = []
for _ in range(M):
    u, v, msg, time = si().split()
    ymd, hms = time.split()
    time_delta = datetime.strptime(time, '%Y%m%d %H:%M:%S') - datetime(1900, 1, 1)
    seconds = int(time_delta.total_seconds())
    logs.append((int(u), int(v), msg, seconds))
# 그래프를 생성하는 방법 1. 인접행렬 2. 인접리스트
con = [[0 for _ in range(N)] for __ in range(N)]
for i in range(M):
    for j in range(i + 1, M):
        if logs[i][1] != logs[j][1]:
            continue
        if logs[i][2] != logs[j][2]:
            continue
        if abs(logs[i][3] - logs[j][3]) >= 600:
            continue
        con[logs[i][0]][logs[j][0]] = 1
        con[logs[j][0]][logs[i][0]] = 1
# 2개의 간선을 건너뛰어야하므로 각 연결된 간선에서, bfs알고리즘을 사용한다
def bfs(start):
    ret = 0
    Q = deque()
    Q.append(start)
    visit = [-1 for _ in range(N)]
    visit[start] = 0
    while Q:
        x = Q.pop()
        if visit[x] == 2:
            break
        for y in range(N):
            if con[x][y] == 1 and visit[y] == -1:
                visit[y] = visit[x] + 1
                ret += 1
                Q.push(y)
    return ret
for i in range(N):
    print(bfs(i), end=' ')