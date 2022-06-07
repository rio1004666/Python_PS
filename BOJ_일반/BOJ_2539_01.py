# 관찰 1. 이분탐색 방향
# 관찰 2. 색종이를 최소한 쓰게하기 위해 정렬후 그리디
# 관찰 3. 1장씩 덮으면서 덮을 수 있는 범위를 벗어나면 그 다음 색종이를 그 위치부터 1장꺼내서 덮어본다
# 관찰 4. 위를 만족하게 하기 위해 하나씩 칠해보는것이아니라 좌표범위안에 포함되는지만 체크하면 되고 인덱스를 증가시켜 나간다
# 관찰 5. 3cm크기 색종이라면 처음 x좌표 1부터 인덱스를 카운팅하면서 3이 되고 4가되는순간 색종이 크기에서 벗어나기때문에 색종이를 추가한다
# 관찰 6. 그리고 색종이를 최소한으로 사용하려면 잘못칠해진 칸의 갯수만큼 반복한다 => 이미 다 덮었다면 빠져나온다
# 관찰 7. 칸을 일일이 false로 만들고 채우기보다 범위로 체크하여 잘못칠해진 칸의 갯수를 카운트해서 비교한다

import sys

si = sys.stdin.readline

N,M = map(int,si().split())

C = int(si())

E = int(si())

left,right = 1,1000001

answer = 0

error = []

######  입력부  #######
for i in range(E):
    row,col = map(int,si().split())
    left = max(left,row)
    error.append((row,col))
#####   입력부  ######

#####   전처리  ######

# x좌표를 기준으로 정렬하고 그 이후에 잘못된 좌표들은 제일 작은 지점부터 필요한부분 덮을것이다

error.sort(key=lambda coord : coord[1])

####    전처리  #####

####   이분탐색  ####

while left < right:
    mid = (left + right) // 2
    cnt = 0
    idx = 0
    while idx < E:
        cnt += 1 # 색종이 하나씩 추가한다
        start_y = 1 # 밑변은 고정이므로 1부터 색종이크기만큼 설정한다
        start_x = error[idx][1] # 잘못색칠한 칸의 x좌표부터 색종이를 덮을 것이다
        i = idx # 잘못색칠된 칸부터 덮을 수 잇는지 체크할것이다
        while i < E and \
            start_y <= error[i][0] < start_y + mid and \
            start_x <= error[i][1] < start_x + mid:
            i += 1 # 색종이 하나로 덮을 수 있는 범위 끝지점까지 인덱스가 이동하고
        idx = i # 덮을 수 없는 지점부터 새로 시작한다
    if cnt <= C:
        right = mid
    else:
        left = mid + 1
####   이분탐색  ####

####   결과 출력 ####

print(right)