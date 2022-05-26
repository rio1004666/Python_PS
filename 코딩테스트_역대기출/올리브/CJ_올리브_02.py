
import sys

si = sys.stdin.readline
W, H, N = map(int, si().split())
cnt = [0 for _ in range(H)]
mem = set()
for _ in range(N):
    x, y = map(int, si().split())
    if (x, y) not in mem:
        mem.insert((x, y))
        cnt[y] += 1  # y층에 "새로운 낙서"가 추가됨

for i in range(H):
    cnt[i] = W - cnt[i]
    cnt[i] += cnt[i - 1]  # cnt[i] = 0~i 층에 대한 총 색칠 넓이
    #        = (0~(i-1)) 층에 대한 총 넓이 + i 층에 대한 추가 넓이
    #        = cnt[i- 1] + cnt[i]
    print(cnt[i], end=' ')
