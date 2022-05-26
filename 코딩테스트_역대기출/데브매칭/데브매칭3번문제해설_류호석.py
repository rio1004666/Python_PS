
# 모든 간선의 길이는 동일
# a에서 b로 가는 최단길이를 생각해볼수잇다...?
# 문제는 가는 도중에 가중치의 합이 넘어버리면 그냥 가지치기한다...?

# 접근방법
# 정점의 개수가 16개이하
# k도 8이하 => 모든 경로를 다해도 할수있다
# 같은점은 두번가지 않는다 !! => 완전탐색 가능!!
# n-2 P k-1 => 시간복잡도
# n-2개중에 k-1개를 순서가 있게 중복없이 나열하는 경우의수
# 16 p 7 => 1730만
# 만약 같은점도 두번갈수있다면 완탐 안된다
# 완전탐색도 최적화 필요하다


# 8 11 0 3 4
# 0 1
# 1 2
# 2 3
# 4 0
# 5 1
# 6 1
# 7 2
# 7 3
# 4 5
# 5 6
# 6 7
import sys

si = sys.stdin.readline
n, m, A, B, K = map(int, si().split())
is_used = [False for _ in range(m)]  # i번째 간선이 사용된 여부
con = [[] for _ in range(n)]
for i in range(m):
    x, y = map(int, si().split())
    con[x].append((y, i))  # (정점의 번호, 간선의 번호)
    con[y].append((x, i))
visit = [0 for _ in range(n)]
path = []  # 사용한 간선의 번호들


def dfs(x, len):
    if len > K:  # 탐색 중단
        return
    if x == B:  # 목적지 도착
        for edge_num in path:
            is_used[edge_num] = True
        return

    visit[x] = True
    for y, edge_num in con[x]:
        # x와 y 연결되어 있고, 그 간선의 번호가 edge_num 인 상황
        if visit[y] == True: continue
        path.append(edge_num)
        dfs(y, len + 1)
        path.pop()
    visit[x] = False


dfs(A, 0)
ans = sum(is_used)
print(ans)
