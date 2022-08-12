# 문제에서는 로봇이 현재 방향이 수평이면 오른쪽 한칸이동하고 1~i,1~i까지 비어있는칸만 우선 채우고  그다음 수직방향으로 틀어서
# 또 그 행동을 반복한다고 어렵게 했지만 시뮬레이션대로 보면 결국 일정한 패턴 규칙이 있다 그것을 그냥 반복문을 사용해서 차근차근 인덱스
# 생각하면서 움지겨주면서 2차원 격자 0으로 전부 셋팅후 숫자1씩 증가시키며 채워나가면 된다
import sys
si = sys.stdin.readline

def solution(N,horizontal):
    answer = [[0 for _ in range(N)] for __ in range(N)]
    answer[0][0] = 1 # 시작은 항상 1로 고정임
    num = 2  # 맨 첫 0,0 위치에서 1을 썻으므로 이제 2를 쓸차례이다
    if horizontal == True: # 수평일때
        for i in range(1,N): # 0,0은 이미 1을 기록했으므로 1부터 시작이다
            if i % 2 == 1: # 홀수 인덱스 즉 1, 3, 5 인경우에는 row 즉 행이 내려감
                row = 0
                # 이 while 반복문은 행이 내려감
                while row <= i: # 항상 대각선에 있는 1,1  2,2   3,3 에서 끝나므로 row와 i가 같아지면 반복문을 break함
                    answer[row][i] = num
                    num += 1 # 예를 들어 숫자 2를 쓰고 3이됨
                    row += 1 # 예를 들어 그 다음 행인 1이됨
                col = i - 1  # 위의 반복문 while은 행이 내려가는 것이고 이번 반복문은 열이 오른쪽으로 간다
                while col >= 0:  #  열이 0이될때까지 반복할 것이다
                    answer[i][col] = num
                    num += 1 # 숫자는 계속 증하가므로 +1 카운팅
                    col -= 1 # 열은 왼쪽으로 가면 감소하므로 -1로 카운팅한다
             # 여기까지 홀수 인덱스일 경우 ㄴ자를 반대로 숫자를 매기는 방식을 하였다 이제 짝수인덱스일 경우는 열부터 오른쪽으로 이동한다
            if i % 2 == 0:  # 짝수번째는 첫열에서 오른쪽으로 i인덱스까지 이동후 거기서 다시 위로 올라감
                col = 0
                while col <= i:
                    answer[i][col] = num
                    num += 1
                    col += 1
                row = i - 1
                while row >= 0:
                    answer[row][i] = num
                    num += 1
                    row -= 1
    elif horizontal == False: # 수직일때
        for i in range(1,N):
            if i % 2 == 1: # 홀수 인덱스 즉 1, 3, 5 인경우에는 위의 수평일 때와는 반대로 하면 된다 즉 열이 오른쪽부터 움직이는것으로 하면된다
                col = 0
                while col <= i:
                    answer[i][col] = num
                    num += 1
                    col += 1
                row = i - 1
                while row >= 0:
                    answer[row][i] = num
                    num += 1
                    row -= 1
            if i % 2 == 0:
                row = 0
                while row <= i:
                    answer[row][i] = num
                    num += 1
                    row += 1
                col = i - 1
                while col >= 0:
                    answer[i][col] = num
                    num += 1
                    col -= 1
    print(answer)
solution(4,True)
solution(5,False)