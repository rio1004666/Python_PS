import collections



def change(d, c):
    # 생각을 해야하는 부분이다 단순히 4방향만 가는 것이아닌 현재 향하는 방향을 알아야한다.
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향

    if c == "L": # 가던방향이 우라면 L로 방향을 틀경우 위로가게된다
        d = (d-1) % 4 # 참고 => -1 % 4 는 3이다 몫이 -1 이되고 나머지가 3이다 4 * -1 + 3 = -1이된다.
    else:
        d = (d+1) % 4
    return d


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve():
    direction = 1 # 방향도 1부터 시작한다.
    time = 1 # 시간 1초 부터 시작한다.
    y, x = 0, 0 # 초기 뱀위치 잡는다.
    visited = collections.deque([[y, x]]) # 방문위치 => 바깥[]는 리스트 자체이고
    # 안쪽 [] 는 y,x를 같이 저장하기 위한 리스트이며 원소이다. 구분해야한다.
    board[y][x] = 2 # 뱀은 2로 표시함
    while True:
        # 우선 범위안에 들고 다음 이동칸이 자신의 몸통이 아닌경우에만 게임을 진행한다.
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < n and 0 <= x < n and board[y][x] != 2:
            if not board[y][x] == 1: # 사과가 없다면

                # 꼬리제거

                temp_y, temp_x = visited.popleft()
                board[temp_y][temp_x] = 0

            board[y][x] = 2
            # 사과가 있든 없든 그다음칸은 뱀머리가 이동되고
            visited.append([y, x]) # 당연히 방문도 추가된다.

            if time in times.keys():

                # 딕셔너리에 등록되어 잇는 시간값이 있다면
                # 방향전환을 한다

                direction = change(direction, times[time]) # 현재바라보고 있는 방향과 전환하고자하는 방향
            time += 1 # 시간은 더해야한다 무조건

        else: # 게임이 종료된다면 시간을 반환한다.
            return time





if __name__ == '__main__':
    n = int(input())
    board = [[0] * n for _ in range(n)]
    k = int(input())
    for _ in range(k):
        y, x = map(int, input().split())
        board[y-1][x-1] = 1
        # 인덱스는 항상 제로베이스부터 명심 또 명심
        # out of index조심 또 조심

    l = int(input())

    # 시간은 딕셔너리에 저장한다 키는 지난시간 값을 방향지정
    # 시간에 해당하는 값을 바로 가져올 수 있으므로 딕셔너리 자료구조를 택한다.
    times = {}
    for _ in range(l):
        t, d = input().split()
        times[int(t)] = d
    # print(board)
    # print(time)
    print(solve())
