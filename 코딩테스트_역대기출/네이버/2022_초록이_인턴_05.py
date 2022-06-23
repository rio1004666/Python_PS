# 각정정의 연결된 정점노드에 적인 수의 합이 간선의 크기이다
# 적절히 노드를 배치해서 간선의 합이 최대가 되게하는 값
# 각 간선의 크기는 노드의 합이라고 보면
# Counting Problem : 간선의 크기를 정점의 크기의 합으로 표현함 다시
# 간선의 크기를 가장 크게 하려면
# 가장 큰노드끼리 가장 많이 연결되도록 하면됨.....
# 각정점마다 연결되어 있는 간선의 수가 되겠다 결국....
# 재배열 부등식
import sys
si = sys.stdin.readline
n, m = map(int, si().split())
deg = [0 for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, si().split())
    deg[u] += 1
    deg[v] += 1
deg.sort()
ans = 0
for i in range(1, n + 1):
    ans += i * deg[i]
print(ans)