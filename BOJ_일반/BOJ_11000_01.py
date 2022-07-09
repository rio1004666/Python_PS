# 그리디 , 우선순위 큐 , 정렬
import sys
from heapq import heappush , heappop
si = sys.stdin.readline

N = int(si()) # 방의 수는 최대 N개가 될것이다 왜냐면 각 각의마다 다른 방에 들어가게되면 최악의 경우가 되기 떄문에 N개가 될것이다
time = []
for i in range(N):
    S,T = map(int, si().split())
    time.append([S,T])
time.sort() # 일단 제일 빠른것부터 봐야하므로 정렬해야한다
room = []
heappush(room,time[0][1])
for i in range(1,N):
    if time[i][0] < room[0]:  # 기존제일 빨리 끝나는 강의보다 더 빠르게 시작해야 한다면 방을 하나 새로 개설한다
        heappush(room, time[i][1])
    else:
        heappop(room) # 기존에 듣던 강의는 방에서 빠지고
        heappush(room, time[i][1]) # 새로운 강의가 방에 들어온다
print(len(room)) # 최종적으로 남아 있는 강의수를 세면 방이 몇갠지 알 수 있다