import sys

si = sys.stdin.readline

N = int(si())
A = [0] + list(map(int, si().split()))
B = [0] + list(map(int, si().split()))

Asum = [ 0 for i in range(N+1)]
Bsum = [ 0 for i in range(N+1)]
Asum[1] = A[1]
Bsum[1] = B[1]
for i in range(2,N+1):
    Asum[i] = Asum[i-1] + A[i]
for i in range(2,N+1):
    Bsum[i] = Bsum[i-1] + B[i]
answer = 0
for i in range(1,N+1):
    if A[i] == B[i]:
        answer += 1
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if Asum[j] - Asum[i-1] == Bsum[j] - Bsum[i-1]:
            answer += 1
print(answer)