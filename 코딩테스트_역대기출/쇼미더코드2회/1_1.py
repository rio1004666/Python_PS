import sys
from itertools import permutations

si = sys.stdin.readline
N,K = map(int,si().split())
monster = list(map(int, si().split()))
people = list(map(int, si().split()))
order = [ i for i in range(N)]

answer = 0
for candis in list(permutations(order,N)):
    mattack = 0
    tpeople = 0
    T = K
    for i in candis:
        if mattack + monster[i] <= T:
            mattack += monster[i]
            tpeople += people[i]
            T -= mattack
            answer = max(answer, tpeople)
        else:
            break
print(answer)
