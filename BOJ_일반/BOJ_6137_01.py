import sys

si = sys.stdin.readline
N = int(si())
arr = []
for _ in range(N):
    ch = ''.join(si().split())
    arr.append(ch)
left,right = 0,N-1
answer = ''
cnt = 0
while left <= right:
    if arr[left] < arr[right]:
        answer += arr[left]
        left += 1
    elif arr[left] > arr[right]:
        answer += arr[right]
        right -= 1
    elif arr[left] == arr[right]:
        left2,right2 = left,right
        differ = False # 다른것이 존재하는지 안하는지 체크하는 변수
        while left2 <= right2:
            if arr[left2] < arr[right2]:
                answer += arr[left]
                left += 1
                differ = True
                break
            elif arr[left2] > arr[right2]:
                answer += arr[right]
                right -= 1
                differ = True
                break
            else:
                left2 += 1
                right2 -= 1
        if not differ: # 다른것이 없다면 그냥 아무거나 넣는다
            answer += arr[left]
            left += 1

    cnt += 1
    if cnt % 80 == 0: # 80번 문자마다 줄바꿈을 넣는다 ( % 활용 )
        answer += '\n'
print(answer)
