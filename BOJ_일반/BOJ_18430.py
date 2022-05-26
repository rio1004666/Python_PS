import sys
si = sys.stdin.readline
n,m = map(int, si().split())
board = [list(map(int, si().split())) for _ in range(n)]
makable = [[False]*m for _ in range(n)]

# brute force 중 backtraking 으로 해결방향을 잡고
# 부메랑 모양이 4가지분이므로 4가지 부메랑 모형을 좌표증감으로 미리 셋팅한다
# 각각 부메랑 모형을 만드는 함수로 생성하여 각 칸마다 부메랑 모양을 만들 수 있는지 전부 체크한다


answer = 0
def Backtracking(i,j,power):

    global answer

    if j == m:
        j = 0
        i += 1
    if i == n:
        answer = max(answer,power)
        return

    if not makable[i][j]:
        if i+1 < n and j+1 < m and not makable[i][j] and not makable[i+1][j] and not makable[i][j+1]:
                makable[i][j],makable[i+1][j],makable[i][j+1] = True,True,True
                npower = power + (board[i][j] * 2) + board[i+1][j] + board[i][j+1]
                Backtracking(i,j+1,npower)

                makable[i][j], makable[i+1][j], makable[i][j+1] = False, False, False
        if i+1 < n and j-1 >= 0 and not makable[i][j] and not makable[i+1][j] and not makable[i][j-1]:
                makable[i][j], makable[i + 1][j], makable[i][j - 1] = True, True, True
                npower = power + (board[i][j] * 2) + board[i + 1][j] + board[i][j - 1]
                Backtracking(i, j+1, npower)

                makable[i][j], makable[i + 1][j], makable[i][j - 1] = False, False, False
        if i - 1 >= 0 and j + 1 < m and not makable[i][j] and not makable[i-1][j] and not makable[i][j+1]:
                makable[i][j], makable[i-1][j], makable[i][j + 1] = True, True, True
                npower = power + (board[i][j] * 2) + board[i - 1][j] + board[i][j + 1]
                Backtracking(i, j+1, npower)

                makable[i][j], makable[i-1][j], makable[i][j + 1] = False, False, False
        if i-1 >= 0 and j-1 >= 0 and not makable[i][j] and not makable[i-1] and not makable[i][j-1]:
                makable[i][j], makable[i - 1][j], makable[i][j - 1] = True, True, True
                npower = power + (board[i][j] * 2) + board[i - 1][j] + board[i][j - 1]
                Backtracking(i, j+1, npower)

                makable[i][j], makable[i - 1][j], makable[i][j - 1] = False, False, False
    # 위의 네가지 경우를 모두 확인후 그 다음칸으로 이동하여 다시 dfs탐색들어간다 ( 모든 경우의수 다 체크해봄 
    Backtracking(i,j+1,power)
Backtracking(0,0,0)
print(answer)