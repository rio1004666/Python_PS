import sys
import heapq
si = sys.stdin.readline
N,M = map(int, si().split())
# 내림차순 정렬한다
times = sorted(list(map(int,si().split())),reverse=True) # 제일 시간 많이 걸리는것부터 꺼내서 heap에다가 넣을것이다
# 제일 시간이 짧은것부터 넣으면 시간이 많이 걸리는것은 순차적으로 끝나야만 충전이 시작되므로 시간이 많이 걸린다
content = []
for t in times:
    if len(content) < M: # 비어있는 콘센트가 있다면 넣어준다
        heapq.heappush(content,t)
    else:
        charged = heapq.heappop(content) # 완충된것은 제거한다
        heapq.heappush(content, charged + t) # 다음 충전할것 push한다 ( 이전에 충전한 시간에 더하여 다음 충전시간을 계산한다
    # 기본 힙은 최소힙이다


print(max(content))