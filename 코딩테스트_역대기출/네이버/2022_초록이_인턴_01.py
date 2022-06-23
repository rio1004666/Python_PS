# 정렬문제
# 1. 그냥 sort
# 2. 종류가 제한되어있기때문에 각각의 갯수를 세어주고 각 문자열을 단순히 A출력하고 B를 출력하고 C를 출력함
# 그럼 시간복잡도는 N이 된다 Counting sort

import sys
si = sys.stdin.readline
si = sys.stdin.readline
n = int(si())
arr = si().strip()
cnt = [0, 0, 0]
for c in arr:
    # 문자열 아스키코드값을 계산하여 인덱스 0부터 채울 수 있게 함
    cnt[ord(c) - ord('A')] += 1
print('A' * cnt[0], end='')
print('B' * cnt[1], end='')
print('C' * cnt[2])
