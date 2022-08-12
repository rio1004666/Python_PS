import sys
import math
sys.setrecursionlimit(10000)
si = sys.stdin.readline
N,K = map(int,si().split())
monster = list(map(int, si().split()))
people = list(map(int, si().split()))
visited = [False for _ in range(N)]
answer = 0

def dfs( K, mattack , ptotal ): # 첫번째 몬스터 잡으러 들어감
    global answer
    if K < 0:
        return
    answer = max(answer, ptotal)
    for i in range(N):
        # 방문하지 않았고 누적 몬스터 공격보다 이상이라면 탐색한다 그렇지 않으면 탐색하지 않고 넘긴다
        if not visited[i]:
            visited[i] = True
            dfs(K - (mattack + monster[i]), mattack + monster[i], ptotal + people[i])
            visited[i] = False
flag = True
for i in range(N):
    if K < monster[i]:
        flag = False
if not flag:
    print(0)
else:
    dfs(K,0,0) # 첫번째 몬스터부터 잡는다
    print(answer)