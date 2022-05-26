
# 대각선행렬로 반전하는 것이 구현량을 줄인다
# 달팽이 문제 => 달팽이 4마리를 만든다
# 흔한 문제는 기본적인 코드가 필요하다
# 그리고 함수화 또는 객체를 하나 생성해서 파라미터에 따른 변화만 받으면 다르게 동작하도록 하는것이 좋은 코드이다
# 여기서 파라미터는 어차피 방향만 바꾸면 알아서 그 방향대로 진행되므로 방향이라는 변수이고 좌표도 각 4개의 지점에서 출발하면 되므로 이것을 파라미터화하는
# 클래스를 만들어서 진행하도록 하였다
# 달팽이하나가 여러개의 파라미터를 받아서 움직이도록 하는 객체지향적 코딩을 하는 것이다.
# 또하나 생각해야할것은 시계방향이냐 반시계방향이냐는 대각선 대칭으로 생각하면된다
# 대각선대칭 출력만해주면 깔끔하게 대각선대칭이된다는것을 확인할 수 있다.


import sys

si = sys.stdin.readline
N = int(si())
move_type = si().strip() # clock, clockwise
dirs = [[0,1], [1,0], [0,-1], [-1,0]]
ans = [[0 for _ in range(N)] for __ in range(N)]

class Snail:
    def __init__(self,x,y,dir) -> None:
        self.x = x
        self.y = y
        self.dir = dir
        self.num = 1
        ans[x][y] = 1
    def move(self) -> bool:
        # 이동할 수 있으면 이동하고, 흔적남기고 True return
        # 이동할 수 없으면 False return 
        nx, ny = self.x + dirs[self.dir][0], self.y + dirs[self.dir][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
            self.dir = (self.dir+1) % 4
        nx, ny = self.x + dirs[self.dir][0], self.y + dirs[self.dir][1]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
            return False
        if ans[nx][ny] != 0:
            return False
        self.x , self.y = nx, ny
        self.num += 1
        ans[nx][ny] = self.num
        return True
snails = [Snail(0,0,0),Snail(0, N-1, 1),Snail(N-1, N-1, 2),Snail(N-1, 0, 3)]
while True:
    flag = False
    for snail in snails:
        flag |= snail.move()
    if not flag:
        break
if move_type == 'clockwise':
    # 대각선 기준으로 반전한다
    for j in range(N):
        for i in range(N):
            print(ans[i][j], end=' ')
        print()
else: # 정방향으로 간다
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end=' ')
        print()


        
    
