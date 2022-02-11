def solution(m, n, board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])

    # 2x2격자에 같은 원소 삭제하기 (set로 원소들의 위치(i,j)와 그 위치들 지운 원소의 갯수(len)를 알수도 있다 = 중복은 제어거이므로 )
    def removeFriends(board):
        remove = [[0] * n for _ in range(m)]
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][
                    j] == board[i + 1][j + 1]:
                    remove[i][j], remove[i][j + 1], remove[i + 1][j], remove[i + 1][j + 1] = 1, 1, 1, 1
        return remove

    def moveFriends(remove, board):
        for i in range(m - 1, -1, -1):  # 거꾸로 올라간다
            for j in range(n):
                if remove[i][j] == 1:  # 비어있는 곳을
                    x = i - 1  # 그 전 행부터 검색해서
                    while x >= 0 and remove[x][j] == 1: x -= 1  # 물건이 있는 위치까지 올라간다
                    if x < 0:  # 물건을 못찾고 범위를 벗어난다면
                        board[i][j] = 0  # 0으로 셋팅한다
                    else:
                        board[i][j] = board[x][j]  # 그 물건을 내린다
                        remove[x][j] = 1  # 공백을 항상 체크해둔다
        return board

    while True:

        remove = removeFriends(board)
        count = 0
        for i in range(m): count += sum(remove[i])
        answer += count
        if count == 0: break
        board = moveFriends(remove, board)

    return answer
print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))