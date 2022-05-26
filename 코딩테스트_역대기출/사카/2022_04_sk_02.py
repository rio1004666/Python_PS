# 1. 모든 단말 노드는 동일한 값을 가지게 하고 싶다
# k가 10이었다면 단말노드들은 두번씩 1을 더해줘서 2로 만들어주고 싶음(총 5개의 노드가 2의값을 가짐 등등 )
# 모든 단말노드는 2라는 조건에 만족
# 2. 단말노드가 아닌 노드들은 자식노드들의 합과 같길 바람
# k가 주어졌을 경우
# 각 정점에 잘 분배해서 이 두가지 조건에 만족하게함
# k = 18일 경우 트리의 각정점을 보관하는 경우가 있을것이다
# k를 바로 배분하려고 하지말고 단말노드는 모두 같은 값을 가지게 될것이라는것을 알고잇으므로
# 단말노드의 값이 1L 이라고 생각하고 각 노드들의 값을 계산한다
# root 부터 dfs적용
# dfs(x) : x를 root로 하는 rooted tree에서
#          x의 모든 자식들의 값 계산  1이냐 3이냐 4냐
# 6 121
# 1 2
# 1 3
# 3 4
# 3 6
# 3 5
import sys
si = sys.stdin.readline
n, k = map(int, si().split())
children = [[] for _ in range(n + 1)]
hasParent = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    par, child = map(int, si().split())
    children[par].append(child)
    hasParent[child] = 1
value = [0 for _ in range(n + 1)]
def DFS(x):
    # x의 모든 자식들에 대해 value 계산해주기
    if not children[x]:  # x 밖에 없는 상황
        value[x] = 1
        return
    for child in children[x]:
        DFS(child)
        value[x] += value[child]
for i in range(1, n + 1):
    if not hasParent[i]:
        DFS(i)
total_value_sum = sum(value)
multiply = k // total_value_sum
for i in range(1, n + 1):
    print(value[i] * multiply, end=' ')