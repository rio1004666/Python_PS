# 여기서도 집을 일일이 설치하려하지말고 거리를 기준으로 집들이 갯수안에 설치 될 수 있는지 판단한다
# 브루트포스로 시간초과날것같으면 역으로 생각하는 것이 최고다
# 최소거리를 1로 잡고 최대거리를 처음집과 마지막집의 차이로 잡는다
# 즉 이분탐색 대상은 최소거리와 최대거리 사이에서 왔다갔다 한다
# 만약 갯수가 넘어가면 거리를 넓혀보고 갯수가 적어지면 거리를 낮추어본다
import sys
si = sys.stdin.readline
N,C = map(int,si().split())
houses = [int(si()) for i in range(N)]
houses.sort()
def get_min_distance(houses,start,end):
    global answer
    while start <= end:
        mid = (start+end) // 2
        current = houses[0]
        count = 1
        for i in range(N):
            if houses[i] >= current + mid:
                count += 1
                current = houses[i]
        if count >= C:

            answer = mid
            start = mid + 1
        else:
            end = mid - 1

start = 1
end = houses[-1]-houses[0]
answer = 0
get_min_distance(houses,start,end)
print(answer)