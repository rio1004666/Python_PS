# 방향을 4방향으로 설정하여 각 방향에 맞게끔 한칸씩 밀어준다
import sys
si = sys.stdin.readline
def rotate(i, R):
    for _ in range(R):
        r,c = i,i
        corners = [(N-1,i),(N-1,M-1),(i,M-1),(i,i)]
        curr = board[r][c]
        d = 0
        while True:
            if d == 4:
                break
            nr,nc = r + dy[d], c + dx[d]
            nxt = board[nr][nc]
            board[nr][nc] = curr
            r,c = nr,nc
            curr = nxt
            # turn
            if nr == corners[d][0] or nc == corners[d][1]:
                d += 1
if __name__ == '__main__':
    N, M, R = map(int, si().split())
    board = [list(map(int, si().split())) for _ in range(N)]
    stage = min(N, M) // 2
    dy = [1, 0, -1, 0]  # 아래 오른 위 왼쪽 순서로 밀것이다 즉 반시계방향으로 한칸씩 이동할것이다
    dx = [0, 1, 0, -1]
    cycle = (N - 1)*2 + (M - 1)*2
    for i in range(stage):
        rotate(i, R % cycle)
        N -= 1
        M -= 1
        cycle -= 8
    for row in board:
        print(*row)