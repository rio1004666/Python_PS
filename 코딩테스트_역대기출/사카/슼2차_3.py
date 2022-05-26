3.
# 3 1
# 1 2
# 2 3
# 1 3
# 3 2
# 0
# 5 0
# 1 2
# 3 1
# 2 4
# 3 5
# 2 1
# 4 1
# 2 5
# 3 2
# 3
# 5 1
# 1 2
# 3 1
# 2 4
# 3 5
# 2 1
# 4 1
# 2 5
# 3 2
# 1
# 7 2
# 3 4
# 7 2
# 5 4
# 2 3
# 6 5
# 1 2
# 2 1
# 3 6
# 1 4
# 1 5
# 7 1
# 3 2
# 2
# 이문제에서 관철은 간선을 삭제하고 추가하는 일련의 연산스킬을 일일이 할 필요가없다
# 간선을 삭제하고 추가할필요없이 간선이 중복이 되지 않은 부분만 추가 삭제할 수 있으므로
# 그렇게 다른부분만 체크해서 카운팅해주면 그것이 연산의 갯수가 된다
# N이 완전작을 경우 완전탐색을 생각해보자 M도 3으로 3번까지 최대 바꿔볼수잇으므로 일일이 다해본다
# 즉 0일때 모든 간선스킬 갯수와
# 1일 때 모든 간선스킬 갯수와..
# 최대 12일때 모든 간선스킬 갯수를 다 일일이 변경하고 중복체크해보는 조합 해본다

import copy
import sys
si = sys.stdin.readline
N, M = map(int, si().split())
treeA = [[0 for _ in range(N + 1)] for __ in range(N + 1)]
# treeA = [] <= 인접리스트로 했을 경우 간선들을 추가할 것이다
treeB = []
# 노드들간의 간선을 연결해주는 인접행렬
for i in range(N - 1):
    x, y = map(int, si().split())
    treeA[x][y] = 1
    treeA[y][x] = 1

# 인접리스트로하면 나중에 중복체크할경우 시간복잡도가 N^2으로 높아진다

# 그래서 위의 인접배열로 그래프를 표현한다

# for i in range(N - 1):
#     x,y = map(int,si().split())
#     treeA.append((x,y))

# 간선들의 정보만 담아도  treea와 비교할 수 있다 간선하나씩 꺼내서

# 여기서 dfs는 그래프 탐색이 아니라 모든 경우의 수 즉 조합을 카운팅해보는 완전탐색이다

# 정점이 존재하냐 안하냐는 인접행렬이 유리하다 (그래프에서 무엇이 궁금하냐에 따라 인접행렬이냐 인접그래프냐 )
for i in range(N - 1):
    x, y = map(int, si().split())
    treeB.append((x, y))

def calc(reorder):
    global treeA, treeB # 전역변수를 함수안에서 사용하기 위해서 global키워드를 사용한다
    B = copy.deepcopy(treeB)
    overlap = 0
    for edge in B:
        u, v = reorder[edge[0]], reorder[edge[1]]
        if treeA[u][v] == 1:  # O(1)
            overlap += 1
    return (N - 1) - overlap  # 간선 스킬 횟수 = (전체 간선 개수) - (겹치는 간선 개수)

ans = 10000

def dfs(used, reorder):  # 가능한 모든 정점스킬 사용 확인을 위한 재귀함수
    # reorder[x]: x 번 정점이 reorder[x]번 정점으로 바뀐다~
    global ans, M
    cnt = calc(reorder)  # 현재 정점스킬 사용 현황에 따른 간선스킬 사용 횟수 계산
    ans = min(ans, cnt)
    if used == M:  # 정점 스킬 다 썼으니까 재귀함수 종료
        return
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            reorder[i], reorder[j] = reorder[j], reorder[i]
            dfs(used + 1, reorder)
            reorder[i], reorder[j] = reorder[j], reorder[i]

# 노드의 순서를 변경할 번호를 담은 리스트를 생성한다

reorder = [i for i in range(N + 1)]

dfs(0, reorder)

print(ans)
