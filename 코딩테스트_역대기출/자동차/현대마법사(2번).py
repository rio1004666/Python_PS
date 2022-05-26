"""
자료구조 맵
2. N , K 주어지면
수열 N개 주어진다

N = 7 K = 3
7 9 11 15 17 19 21 100
k=3이므로 2차이가 3번등장하면 다 지워진다
그래서 맵자료구조로 푼다

"""
# 8 3
# 24 22 20 10 5 3 2 1
# 정답: 3
from collections import defaultdict
import sys
si = sys.stdin.readline
N, K = map(int, si().split())
a = list(map(int, si().split())) # 배열은 내림차순정렬되어 나온다고 했으므로
# 앞에서부터 차이를 담아보면된다
diff = defaultdict(list)
for i in range(0, N - 1):
    diff[a[i] - a[i + 1]].append(i)
for v in diff.values(): # 자료구조 맵에서 값인 리스트를 불러와서
    if len(v) >= K: # k이상인 갯수가 있다면
        for idx in v: # 그것들을 하나씩 불러와서
            a[idx] = 0 # 없애준다
            a[idx + 1] = 0 # 그다음것도 없애준다
ans = 0
for i in range(N):
    if a[i] != 0:
        ans += 1
print(ans)