# 센서N개 주어지면 집중국 K개로 분할했을경우 수신할수있는 영역의 최소의 합을 구하기

import sys

si = sys.stdin.readline
N = int(si())
K = int(si())
sensors = sorted(list(map(int, si().split())))
if K >= N:
    print(0)
    sys.exit()
dist = []
for i in range(1,N):
    dist.append(sensors[i]-sensors[i-1])
dist.sort(reverse=True)
for _ in range(K-1):
    dist.pop(0)
print(sum(dist))