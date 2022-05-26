1.
# 4
# pencil
# cilicon
# contrabase
# picturelist
import sys
from collections import defaultdict
si = sys.stdin.readline
N = int(si())
strs = [si().strip() for _ in range(N)]
cnt = defaultdict(int)
for str in strs:
    substrs = set()
    m = len(str)
    for i in range(m):
        for j in range(i, m):
            substrs.add(str[i:j + 1])
    for substr in substrs:
        cnt[substr] += 1

# cnt[x] := x가 전체 문자열에 걸쳐서 부분문자열로 등장하는 횟수

for str in strs:
    m = len(str)
    flag = False
    for length in range(1, m + 1):  # 부분문자열의 길이
        ans = set()
        for i in range(m - length):  # 부분문자열의 시작 위치
            substr = str[i:i + length]
            if cnt[substr] == 1:  # 이 부분문자열은 유니크하다는 의미
                ans.add(substr)
        if ans:
            flag = True
            ans = sorted(list(ans))
            for substr in ans:
                print(substr, end=' ')
            print()
            break
    if not flag:
        print('None')
