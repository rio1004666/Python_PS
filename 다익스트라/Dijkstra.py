from typing import List
import collections
import heapq


def networkDelayTime(times: List[List[int]], N: int, K: int) -> int:
    # 키가 있는 경우는 밸류가 있겠지만 키가 없는 경우  디폴트 값으로 [] 리스트가 자동생성된다
    # 그래서 반복문에서 딕셔너리 크기가 변동 되는 오류가 발생할수 있으므로 list()로 고정시킨후에 반복문을 실행시키는 것이 좋다.
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    dist = collections.defaultdict(int)
    Q = [(0, K)]  # 우선순위 큐를 생성한다 우선 출발 노드는 거리가 0인 튜플로 시작한다
    while Q:  # Q안에 원소가 빌때까지 반복한다.
        time, node = heapq.heappop(Q)  # Q를 힙자료구조로 넣었다 뺏다할 수 있도록 한다.
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))  # 대상과 값을 같이 지정해준다.
    if len(dist) == N:
        return max(dist.values())
    return -1


print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
