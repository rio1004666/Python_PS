import heapq
input = __import__('sys').stdin.readline

m = int(input())
l = [0]+list(map(int,input().split()))
l.sort()
n = int(input())

H = []
for i in range(m): heapq.heappush(H,(0,l[i+1]))
for i in range(m):
    if l[i+1]-l[i]-1<=n: # 포함하지 않는 정수들이 n개까지는 그냥 모든 정수에 대한 구간의 갯수를 구한다
        for j in range(l[i]+1,l[i+1]): heapq.heappush(H,((j-l[i])*(l[i+1]-j)-1,j))
    else:
        for j in range(l[i]+1,l[i]+1+n//2+1): heapq.heappush(H,((j-l[i])*(l[i+1]-j)-1,j))
        for j in range(l[i+1]-1,l[i+1]-1-n//2,-1): heapq.heappush(H,((j-l[i])*(l[i+1]-j)-1,j))
for i in range(n-len(H)): heapq.heappush(H,(float('inf'),l[-1]+1+i))
for i in range(n): print(heapq.heappop(H)[1], end=' ')