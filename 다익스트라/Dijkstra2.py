import collections
from typing import List
import heapq


# 그런데 이 코드는 어느 순간 사이클이 돌아버려서 무한시간대가 된다. 이것을 주의해야한다.
# 그래서 이미 방문한곳은 방문하지 않는다는 원칙을 세운다 => 우선순위큐로 최소값만 추출했기때문에 가능한것이다!!!


def findCheapestPrice(n: int, flight: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flight:
        graph[u].append((v, w))
    Q = [(0, src, K)]

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:  # 한 노드를 거쳐갈때마다 -1 하고 0이되면 총 거쳐가는 노드수를 만족하게 되므로 다음 노드를 방문할 것이다,.
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k - 1))
    return -1


def findCheapestPrice2(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))
    visit = {}
    Q = [(0, src, K)] # 초기값에 거쳐가는 노드를 나타내는 변수를 정해준다.
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if node not in visit or visit[node] > k: # 기존의 방문했던 노드의 방문 횟수보다 작아야한다 => 같은 2번노드라도 k가 1이거나 2일 수 있다(거쳐가는 노드수)
            visit[node] = k
            for v, w in graph[node]:
                if k <= K: # 여기서 필터링시킨다. 총 K번 거쳐가야하는데 지나치면 더이상 힙에 넣지않고 패스한다.
                    # K가 5라면 k 가 2가 되어도 2번노드에 도착하면 조건을 만족하므로 답이 바뀐다.
                    # K가 1이라도 1번 거쳐간다는 의미이므로 이 필터링을 통과해서 우선순위큐에 넣는다.
                    heapq.heappush(Q, (price + w, v, k + 1)) # k를 카운팅시켜서 거쳐가는 노드수를 1증가시켜서 힙에 넣어준다
    return -1
