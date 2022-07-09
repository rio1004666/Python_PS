# N 파일 사용기록 ( day , idx ,time )
# R일 내에 Ru시간 이하
# 총 사용을 Rt시간 미만
# 두 조건이 만족되면 확정
# 그 번호를 출력
# 파일은 100개까지 가능
# 각 제품별로 시간을 저장할 배열 자료구조로서
# 사용기록을 입력받으면서 각 제품별 사용시간을 알 수 있다
# 그에 부합하는 제품 출력

import sys
si = sys.stdin.readline
n, Q, recent_day, recent_use, total_use = map(int, si().split())
recent = [0 for _ in range(n + 1)]
total = [0 for _ in range(n + 1)]
for _ in range(Q):
    day, idx, time = map(int, si().split())
    if day <= recent_day:
        recent[idx] += time
    total[idx] += time
ans = []
for i in range(1, n + 1):
    if recent[i] <= recent_use and total[i] < total_use:
        ans.append(i)
print(len(ans))
print(*ans)
