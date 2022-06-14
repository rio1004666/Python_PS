from collections import deque


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    result = 1
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                result += 1
                queue.append(nxt)
    return result


def solution(n, wires):
    # 노드들을 방문하면서 갯수를 센다
    # 100-1개의 간선을 순회하므로 방문표시하면 시간복잡도는 v+u 만큼 걸린다
    answer = n  # 정답 초기값 설정
    graph = [[] for _ in range(n + 1)]  # 노드는 1부터 시작한다
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
    # n제한 100개뿐이므로 n-1개의 간선을 하나씩 제거해본다
    for start, not_visit in wires:
        visited = [False for _ in range(n + 1)]
        visited[not_visit] = True
        # 한쪽만 탐색하고 나머지는 총갯수에서 빼면 시간복잡도를 줄일 수 있다
        result = bfs(start, graph, visited)
        if abs(result - (n - result)) < answer:
            answer = abs(result - (n - result))

    return answer