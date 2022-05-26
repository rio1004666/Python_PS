
2.
def find_place(n, m, board, l):
    for i in range(m - l + 1):
        for j in range(n - l + 1):
            cnt = 0
            for ni in range(i, i + l):
                for nj in range(j, j + l):
                    cnt += board[ni][nj]
            if cnt == 0:
                for ni in range(i, i + l):
                    for nj in range(j, j + l):
                        board[ni][nj] = 1
                return (j, i, l)
    return None
def solution(n, m, rectangle):
    rectangle.sort(key=lambda x: x[0])
    board = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
    answer = []
    for l, cnt in rectangle:
        for _ in range(cnt):
            coord = find_place(n, m, board, l)
            if not coord:
                continue
            answer.append(coord)
    return answer