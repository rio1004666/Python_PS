# https://www.acmicpc.net/problem/1379
# 접근 방법
# 강의 정보를 강의 시간을 기준으로 정렬한다.
# 강의 정보를 반복문을 통해 하나씩 확인한 뒤, 해당 강의의 종료시간과 강의실 번호를 힙에 넣는다.
# 이때 힙에 저장되어있는 종료 시간 중, 현재 탐색 중인 강의의 시작시간보다 작거나 같은 경우 모두 뺀다.
# 매 탐색마다 힙의 길이만큼의 인덱스에 해당하는 것을 강의실 번호로 매겨 이를 강의실 번호를 기준으로 하는 리스트에 저장한다.
# 또한 각 강의실 중 비어있는 위치는 강의실에 대한 minHeap을 통해 구한다.

import sys, heapq
input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
lecture = [0 for _ in range(n+1)]
arr.sort(key=lambda x: (x[1], x[2])) # 시작시간이 제일 빠르고 그다음 제일 빨리 끝나는 강의순으로 정렬한다
room = []
for i in range(1, n+1):
    heapq.heappush(room, i) # 강의방 번호를 입력받는다
minHeap = [] # 최소힙으로 가장 빨리 끝나는 강의는 빼버리고 그다음 강의를 넣는다
print(arr)
for x in arr:
    while minHeap and minHeap[0][0] <= x[1]: # 제일 빨리 끝나는 전강의가 다음 강의 시작시간보다 빨리 끝난다면
        end, r = heapq.heappop(minHeap)
        heapq.heappush(room, r) # 방에 들어간다
    # 방번호를 1번부터 5번까지 돌려쓴다 강의실방을 그래서 5가 최소 필요한 강의실수이다
    # 계속 작은 방번호부터 사용할것이다
    r = heapq.heappop(room) # 강의가 종료된방에서 강의를 빼고
    heapq.heappush(minHeap, [x[2], r]) # 제일 빨리 시작하는 방의 종료시간과 강의방 1번부터 차례로 넣어준다
    lecture[x[0]] = r # 해당 강의번호에 빈 강의방을 기록한다


print(max(lecture))
for x in lecture[1:]:
    print(x)