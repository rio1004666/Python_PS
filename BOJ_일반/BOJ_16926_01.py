# r의 값이 10억이라하더라도 rotate로 별차이없다
# 이것도 큐를 사용하긴 하는데 r의범위가 10억이라도 시간 소모가 적게걸린다
from collections import deque


def rotate_board(r):
    global N, M, board
    q = deque()
    _width, _height = M, N
    time = min(_width, _height) // 2
    nx, ny = 0, 0

    while time >= 1:
        for i in range(_width-1):
            q.append(board[ny][nx+i])
        for i in range(_height-1):
            q.append(board[ny+i][nx+_width-1])
        for i in range(_width-1):
            q.append(board[ny+_height-1][nx+_width-1-i])
        for i in range(_height-1):
            q.append(board[ny+_height-1-i][nx])

        q.rotate(-r)

        for i in range(_width-1):
            board[ny][nx+i] = q.popleft()
        for i in range(_height-1):
            board[ny+i][nx+_width-1] = q.popleft()
        for i in range(_width-1):
            board[ny+_height-1][nx+_width-1-i] = q.popleft()
        for i in range(_height-1):
            board[ny+_height-1-i][nx] = q.popleft()
        # 가로 세로 너비는 더 작아짐
        _width -= 2
        _height -= 2
        # 돌리기 시작하는 첫 위치는 대각선 오른쪽 방향 내려감
        nx += 1
        ny += 1
        # time은 돌릴때마다 테두리가 안으로 들어가면서 돌리므로 한계가 올때까지 돌리는 수의 카운트이다
        time = min(_width, _height) // 2


N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
rotate_board(R)
for i in range(N):
    print(*board[i])