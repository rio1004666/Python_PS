# 문제를 푸는 습관 => 1. 이 문제는 어떠한 방향으로 풀이를 원하는지
# 문제를 푸는 습관 => 2. 관철 애드혹 아이디어
# 문제를 푸는 습관 => 3. 문제이해 및 제한사항 확인
# 문제를 푸는 습관 => 4. 어떤 자료구조와 알고리즘이 쓰이는지 확인
# 문제를 푸는 습관 => 5. 인풋과 아웃풋 확인
# 문제를 푸는 습관 => 6. 구현력
# n제한 50 => 브루트 포스 => 전부 빈칸에 퍼즐을 맞춰본다 => 그런데 각 빈칸을 전부 퍼즐 하나씩 돌려가며 맞춰보면 시간이 상당히 걸린다 그래서 여기서 떠오른 생각은 퍼즐모양을 기준을 0,0으로 잡고 보드판위의 모양과 테이블위에 있는 퍼즐모양과 같다면 보드판의 빈칸좌표를 빼고 그 갯수를 카운팅하면 된다 즉 좌표를 0,0으로 전부 통일하는 것이다 그러면 퍼즐전부를 게임보드판에 맞출필요가 없다
# 1. 게임보드의 모양을 구한다.

#     모양은 2차원 배열의 좌표 순서대로 찾으며, 방문하지 않고 해당 값이 0일 때의 좌표를 기준으로 (0,0)로 모양을 찾음

#     시작점을 찾고 나면 U, D, R, L 좌표를 더해보며 이동할 수 있는지 확인(좌표가 값을 넘어가는지, 방문했는지, 값이 0)

#     이동할 수 있으면  값을 추가해줌

# 2. 퍼즐 조각의 모양을 구한다.

#     로직은 동일하며 퍼즐 조각은 회전할 수 있으므로 4번 회전시켜보며 조각 값을 구한다.

# 3. 게임보드 빈공간의 모양과 퍼즐 조각의 모양이 일치하면 해당 퍼즐 조각은 테이블에서 차있는 것으로 초기화
def rotate(table):
    return list(map(list, zip(*table[::-1])))


def dfs(condition, table, key, value, visited):
    i, j, x, y, target = condition
    visited[i][j] = 1
    key.append((i, j))
    value.append((x, y))
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]  # U D R L
    for move in moves:
        dx, dy = move
        move_x, move_y = i + dx, j + dy
        if move_x < 0 or move_y < 0 or move_x >= len(table) or move_y >= len(table):
            continue
        elif table[move_x][move_y] == target and visited[move_x][move_y] == 0:
            key, value, visited = dfs([move_x, move_y, x + dx, y + dy, target], table, key, value, visited)
    return key, value, visited


def puzzle(table, target):
    visited = [[0] * len(table) for _ in range(len(table))]
    pieces = {} if target == 1 else []
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == target and visited[i][j] == 0:
                key, value, v = dfs([i, j, 0, 0, target], table, [], [], visited)
                if target == 1:
                    pieces[tuple(key)] = value
                else:
                    pieces.append(value)
                visited = v
    return pieces


def solution(game_board, table):
    # 이 풀이에서는 좌표들이 존재하냐 안하냐를 확인했음 일일이 넣어보는것이아닌
    answer = 0
    board = puzzle(game_board, 0)  # 퍼즐모양들의 위치값을 각각 구함 (0,0을 기준으로) 타켓은 게임보드이냐 테이블이냐 구분하기 위한 플래그 변수이다

    print(board)
    print('--------------------------------------------------------------------')
    for _ in range(4):  # 4방향으로 돌림
        table = rotate(table)  # 테이블 자체를 돌려버림
        pieces = puzzle(table, 1)  # 다시 테이블에 있는 퍼즐조각을 수집함
        print(pieces)
        # 키는 원래 좌표위치이고 그 키로 다시 0,0위치에서 dfs탐색을 통해 게임보드 빈칸 좌표와 맞춘다
        for key, value in pieces.items():
            if value in board:  # 그 퍼즐조각들이 보드에 전부 존재한다면
                board.remove(value)  # 보드의 빈칸 좌표들을 제거함
                answer += len(value)  # 빈칸좌표들의 갯수를 정답에 추가
                for cod in key:
                    i, j = cod
                    table[i][j] = 0
    return answer