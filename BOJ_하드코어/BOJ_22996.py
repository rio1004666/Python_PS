__import__('sys').setrecursionlimit(423123)
input = __import__('sys').stdin.readline
MIS = lambda: map(int,input().split())

n, Q = MIS()
print(n, Q)

par = list(MIS())
adj = [[] for i in range(n+1)]
for i in range(n): adj[par[i]].append(i+1)
Q2 = int(input())
for i in range(Q2): print(2, int(input()))
Q-= Q2

def dfs(v):
    global Q
    for u in adj[v]:
        if v == u: continue
        dfs(u)
        Q-= 1
        print(1, u, v)

for i in range(n):
    if par[i] == i+1: root = i+1; dfs(i+1)
for i in range(Q): print(1, root, root)