import sys

si = sys.stdin.readline

d, n, m = map(int, si().split())

stone = [int(si()) for _ in range(n)]
stone.sort()
start = 0
end = d
dist = 0
while start <= end:
    # 이분탐색으로 시간을 현저히 줄임
    mid = (start + end) // 2
    count = 0
    now = 0
    min_distance = d
    # 5만개의 돌을 체크
    for x in stone:
        # 현재 기준이되는 최소거리를 갱신해간다
        if x - now >= mid: # 기준 최소거리보다 크면 제거하지 못함
            min_distance = min(min_distance, x-now)
            now = x
        else: # 작으면 돌을 제거함
            # 돌을 제거하는 갯수를 카운팅
            count += 1

    min_distance = min(min_distance , d - now)

    if count > m:
        end = mid - 1
    else:
        # 최소거리의 최대를 찾으면 됨
        dist = max(dist, min_distance)
        start = mid + 1

print(dist)