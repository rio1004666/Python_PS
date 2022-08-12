
# bfs 풀이 + 그냥 전부 회전시켜서 맞춰보는 풀이....
# 너무 많은 for문 소모 => 9초대 나오는것도 존재
# 하지만 이러한 나이브한 풀이라도 해야함 => 정확도만이라도
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def rotation(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    result = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n-1-r] = puzzle[r][c]

    return result


def bfs(i, j, table, check):
    puzzle = []
    n = len(table)
    q = [(i, j)]
    check[i][j] = True
    while q:
        x, y = q.pop()
        puzzle.append([x, y])
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not check[nx][ny] and table[nx][ny] == 1:
                q.append((nx, ny))
                check[nx][ny] = True

    return puzzle


def trans_puzzle(puzzle_location):
    r_min, r_max = 100, -1
    c_min, c_max = 100, -1
    for location in puzzle_location:
        r, c = location
        r_min = min(r_min, r)
        r_max = max(r_max, r)
        c_min = min(c_min, c)
        c_max = max(c_max, c)

    r_len = r_max - r_min + 1
    c_len = c_max - c_min + 1
    trans = [[0] * c_len for _ in range(r_len)]
    for location in puzzle_location:
        x = location[0] - r_min
        y = location[1] - c_min
        trans[x][y] = 1

    return trans


def empty_side(game_board, puzzle, i, j):
    n = len(game_board)
    for x in range(len(puzzle)):
        for y in range(len(puzzle[0])):
            if puzzle[x][y] == 1:
                for k in range(4):
                    nx, ny = x + i + dx[k], y + j + dy[k]
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if game_board[nx][ny] != 1:
                        return True

    return False


def is_match(puzzle, game_board):
    n = len(game_board)
    r = len(puzzle)
    c = len(puzzle[0])
    for i in range(n-r+1):
        for j in range(n-c+1):
            match = True
            for x in range(len(puzzle)):
                for y in range(len(puzzle[0])):
                    game_board[x+i][y+j] += puzzle[x][y]
                    if game_board[x+i][y+j] != 1:
                        match = False

            if empty_side(game_board, puzzle, i, j):
                match = False

            if match:
                return True
            else:
                for x in range(len(puzzle)):
                    for y in range(len(puzzle[0])):
                        game_board[x+i][y+j] -= puzzle[x][y]

    return False


def solution(game_board, table):
    n = len(game_board)
    answer = 0
    puzzles = []
    check = [[False] * n for _ in range(n)]
    puzzle_sum = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not check[i][j]:
                puzzle_location = bfs(i, j, table, check)
                puzzle = trans_puzzle(puzzle_location)
                puzzles.append(puzzle)
                puzzle_sum.append(len(puzzle_location))

    for idx, puzzle in enumerate(puzzles):
        for _ in range(4):
            puzzle = rotation(puzzle)
            if is_match(puzzle, game_board):
                answer += puzzle_sum[idx]
                break

    return answer