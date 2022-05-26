"""Solution code for "BOJ 1944. 복제 로봇".

- Problem link: https://www.acmicpc.net/problem/1944
- Solution link: http://www.teferi.net/ps/problems/boj/1944
"""

import heapq

DELTAS = ((-1, 0), (1, 0), (0, -1), (0, 1))
START = 'S'
KEY = 'K'
WALL = '1'
INF = float('inf')


def main():
    N, M = [int(x) for x in input().split()]
    grid = [input() for _ in range(N)]

    for r, row in enumerate(grid):
        if (c := row.find(START)) >= 0:
            start_row, start_col = r, c
            break

    tot_dist = 0
    found_keys = 0
    dists = [[INF] * N for _ in range(N)]
    dists[start_row][start_col] = 0
    heap = [(0, start_row, start_col)]
    while heap:
        dist, r, c = heapq.heappop(heap)
        if dist > dists[r][c]:
            continue
        if grid[r][c] == KEY:
            tot_dist += dist
            found_keys += 1
            dists[r][c] = 0
            new_dist = 1
        else:
            new_dist = dist + 1
        for dr, dc in DELTAS:
            nr, nc = r + dr, c + dc
            if (0 <= nr < N and 0 <= nc < N and grid[nr][nc] != WALL and
                    new_dist < dists[nr][nc]):
                dists[nr][nc] = new_dist
                heapq.heappush(heap, (new_dist, nr, nc))

    print(tot_dist if found_keys == M else '-1')


if __name__ == '__main__':
    main()
