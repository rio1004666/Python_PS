import sys

si = sys.stdin.readline

N,M = map(int, si().split())
result = []
def dfs(pos):
    if len(result) == M:
        print(' '.join(map(str,result)))

    for i in range(pos,N+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()
dfs(1)