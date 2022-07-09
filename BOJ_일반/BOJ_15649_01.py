import sys
import copy
si = sys.stdin.readline

N,M = map(int, si().split())

result = []

def dfs():
    if len(result) == M:
        print(' '.join(map(str,result))) # 리스트에 있는 모든 원소를 문자열로 바꿈
        return
    for i in range(1,N+1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()
dfs()
for row in result:
    for el in row:
        print(el , end=' ')
    print()