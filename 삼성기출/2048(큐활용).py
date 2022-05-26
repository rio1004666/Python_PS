import collections
from copy import deepcopy

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]


def rotate(n, board):
    new_board = deepcopy(board)
    for row in range(n):
        for col in range(n):
            new_board[col][n - row - 1] = board[row][col]  # 0,2 가 2.3으로 된다
    return new_board


def merge(n, row):
    queue = collections.deque([num for num in row if num != 0])
    new_list = []
    flag = False
    while queue:
        num = queue.popleft()
        if len(new_list) == 0:  # 처음 들어오는 원소는 바로 넣어버린다.
            new_list.append(num)
        else:  # 그다음 원소부터는 마지막에 넣은 원소와 현재 빼낸 원소와 비교해보고 같으면 마지막원소를 2배로하고 플래그 트루로 바꿔버린다.
            if new_list[-1] == num and not flag:  # 오직 합친적이 없고 같은 원소일 경우에만 합친다.
                new_list[-1] *= 2
                flag = True  # 그 전원소가 한번 합쳣다는것을 체크해주기 위한 스위치 변수이다.
            else:  # 그냥 원소가 들어간다면 플래그 변수 해제한다. 그다음원소부터는 다시 같다면 합쳐버린다.
                new_list.append(num)
                flag = False
    return new_list + [0] * (n - len(new_list))


def dfs_search(n, board, count):
    # 다음 판 넘어가기전에 현재 보드판의 블럭중에서 최댓값을 설정하고 그 다음 4방향 기울어서 나오는 최댓값과 비교해본 후 최댓값을 최종적으로 결정한다.
    result = max([max(row) for row in board])
    if count == 0:
        return result
    for _ in range(4):
        merged_board = [merge(n, row) for row in board]
        result = max(result, dfs_search(n, merged_board, count - 1))
        board = rotate(n, board)
    return result # 위의 4방향에서 최종적으로 최댓값이 결정되면 최댓값을 마지막으로 반환한다.


final = dfs_search(n, board, 5)
print(final)
