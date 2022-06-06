import sys
import math
si = sys.stdin.readline
N,A = map(int, si().split())
rooms = [list(map(int, si().split())) for _ in range(N)]
left = 1
right = int(1e18)
answer = 0
while left <= right:
    mid = ( left + right ) // 2
    hp,attack = mid, A # 최소 HP와 공격력 초기화
    for i in range(N):
        t,a,h = rooms[i][0], rooms[i][1], rooms[i][2]
        if t == 1:
            hp -= (math.ceil(h/attack)-1) * a
            if hp <= 0:
                break
        else:
            hp = min(mid , hp + h) # 최대 hp를 넘을 수는 없으므로 넘어가면 최대 hp값을 설정한다
            attack += a
    if hp > 0:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)


