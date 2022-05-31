# 생각의 방향 시작점과 끝지점을 나누어 생각함 => 분류
# 시작점을 만나면 끝지점을 최대힙에 넣을것이다
# 시작점이 전 기준점보다 크면 무조건 변동점이 생기므로 결과리스트에 넣는다
# 다시 기준점을 업데이트한다
# 기준점보다 높이가 작다면 스카이라인에 포함안되므로 결과리스트에 넣지 않는다
# 이제 끝지점이 돌기시작하면 차례로 자기보다 작은 높이에 잇는 끝지점들을 다꺼내본다
# 없다면 그다음 끝지점으로 간다
# 또 없다면 그 다음 끝지점으로 간다
# 이제 이것이 제일 높은 직사각형의 끝지점이라면 큰것부터 하나씩 전부 끄집어내서 변동지점을 결정해서 결과리스트에 넣는다

import sys, heapq

# 입력부
n = int(sys.stdin.readline())
arr = []
height = [0] * n
q = []

# end : 현재 index번째 건물의 끝나는 지점을 저장하는 리스트
end = [0] * n
# check : 현재까지 끝난 끝점을 저장하는 set
check = set()
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    # 시작점이면 1, 끝점이면 -1
    arr.append((a, i, 1))
    arr.append((c, i, -1))
    height[i] = b
    end[i] = c
# 그림 2, 그림3에 따라 정렬
# 첫번째 우선순위 : 시점이 앞서는지
# 두번째 우선순위 : 시점이 같다면 시작점인지
# 세번째 우선순위 : 시점도 같고 둘 다 시작점이면 높이가 더 높은지
arr.sort(key=lambda x: (x[0], -x[2], -height[x[1]]))

# now : 현재 최고높이
now = 0
ans = []
print(arr)
for i in range(len(arr)):
    # point : 시점, idx : 건물의 인덱스, dir : 시작점인지 끝점인지
    point, idx, dir = arr[i]

    # 시작점인 경우(빨간점)
    if dir == 1:
        # 높이가 갱신된다면 그 부분이 새로운 스카이라인
        if now < height[idx]:
            now = height[idx]
            ans.append((point, now))
        # 높이가 갱신됨과 상관없이 현재 건물의 높이와 끝점을 최대 힙에 저장
        heapq.heappush(q, (-height[idx], end[idx]))

        print('끝점담기 ', q)
    # 끝점인 경우(파란점)
    else:
        # 현재 시점이 끝났기 때문에 set에 끝점의 시점을 저장
        check.add(point)
        # 최대 높이가 끝난 건물이 아닐때까지 pop

        print(check)
        # 여태까지 저장된 끝점들을 꺼낸다 단, 끝나지 않은점은 아직 남아있다
        while q:
            if q[0][1] not in check: #
                break
            heapq.heappop(q)
        print(point,'가',' 힙팝끝낸후 ', q)
        # 힙이 비었다면 스카이라인의 높이는 0으로 갱신
        if not q:
            if now:
                now = 0
                ans.append((point, now))

        # 힙이 있다면 현재 높이와 비교 시 변동이 있다면 그 높이가 그 다음으로 높은 건물이기 때문에
        # 스카이라인 높이 갱신
        else:
            if -q[0][0] != now:
                now = -q[0][0]
                ans.append((point, now))

# 정답 출력
for i in ans:
    print(i[0], i[1], end=' ')