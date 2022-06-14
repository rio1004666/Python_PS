from collections import defaultdict, deque


def bfs(start_point, cut_point, wires, n, wire_dict):
    count = 0
    visited = [False] * (n + 1)
    q = deque([start_point])
    visited[start_point] = True

    while q:
        p = q.popleft()
        for next_p in wire_dict[p]:
            if next_p == cut_point: continue
            if visited[next_p] is True: continue
            count += 1
            q.append(next_p)
            visited[next_p] = True

    return count


def solution(n, wires):
    answer = 100000
    # dictionary로 그래프 자료구조 저장
    wire_dict = defaultdict(set)
    for wire in wires:
        wire_dict[wire[0]].add(wire[1])
        wire_dict[wire[1]].add(wire[0])

    # wire 하나를 끊는 모든 경우의 수에 대해 bfs로 조사
    for wire in wires:
        v1 = wire[0]
        v2 = wire[1]
        diff = abs(bfs(v1, v2, wires, n, wire_dict) - bfs(v2, v1, wires, n, wire_dict))
        answer = min(diff, answer)  # 두 전력망이 가지고 있는 송전탑 개수의 차이의 최소값 갱신

    return answer