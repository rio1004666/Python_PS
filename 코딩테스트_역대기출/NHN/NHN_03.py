import sys
si = sys.stdin.readline
N, L, Q = map(int, si().split())
langs = [list(map(int, si().split()))[1:] for _ in range(N)]
lang_map = [[0 for _ in range(L)] for __ in range(N)]  # lang_map[i][l] := i번 사람이 l 번 언어를 아느냐?
# 2차원 배열로 시간복잡도를 현저하게 1로 만든다 난 SET로 두 사람간의 중복이 있냐로 판단해서 접근하려고 하였다
# 하지만 이렇게 배열로 자료구조를 잡으면 각 두 사람과의 교차점은 언어이므로 두사람씩 짝을 지어서 이 언어를 공통적으로 알고 있냐고 판단하는데는 N^3으로 걸린다
# SET로 했을 경우에는 두 사람의 모든 언어를 비교하게 되므로 N^4가 된다 한사람의 언어에대해 다른 사람의 모든 언어를 탐색하므로
# 또 해설에서는 사람명이 문자열이아니라 숫자로 하였다 문자열로 처리하려면
# 해시맵을 사용할 수 밖에 없다
# 그래서 해시맵으로 숫자를 0부터 차례로 증가시키면서 그 사람이름을 매핑시켜주면 된다 {"A": 0 , "B": 0} 단순히 대문자였다면 아스키코드값 계산으로 숫자인덱스를 만들 수 있겠지만....여러개의 문자복합이다
# 인접행렬 그래프 장점 : 노드 i와 노드 j가 연결되어 있는지 확인하고 싶을 때, adj[i][j]가 1인지 0인지만 확인하면 되기 때문에 O(1)이라는 시간 복잡도에 확인할 수 있다는 점이 있습니다. 
# 노드의 개수에 비해 간선의 개수가 훨씬 적은 그래프라면 모든 노드의 갯수를 다 확인해야한다...... 이게 단점 => 인접리스트 그래프
# 이 문제에서도 인접행렬 그래프를 사용하는 것은 첫재로 두 노드간의 연결을 확인만하는데 사용하고 노드끼리 다 연결될 수 있다는 점에서 인접행렬 그래프를 사용한다
for i in range(N):
    for l in langs[i]:
        lang_map[i][l - 1] = 1
# construct graph
INF = 100000000
con = [[INF for _ in range(N)] for __ in range(N)]
for i in range(N):
    con[i][i] = 0
    for j in range(i + 1, N):
        # i 라는 사람과 j 라는 사람이 대화가 가능하냐? 가능하면 간선을 연결함
        # 여기서 그래프를 인접행렬로 연결함 => 모든 사람들끼리 간선 연결이 될 수 있음
        for lang in range(L):
            if lang_map[i][lang] == 1 and lang_map[j][lang] == 1:
                con[i][j] = con[j][i] = 1
                break
# floyd-warshall algorithm => BFS알고리즘보다 시간복잡도가 낮음 => 인접행렬로 그래프를 형성했을 경우 사용
for k in range(N):
    for i in range(N):
        for j in range(N):
            if con[i][k] == INF or con[k][j] == INF: continue
            con[i][j] = min(con[i][j], con[i][k] + con[k][j])
for _ in range(Q):
    x, y = map(int, si().split())
    x -= 1
    y -= 1
    if con[x][y] == INF:
        print(-1)
    else:
        print(con[x][y] - 1)
