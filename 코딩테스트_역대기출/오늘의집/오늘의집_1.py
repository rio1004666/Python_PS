# 1. 동쪽 - 1번 남쪽 - 2번 서쪽 - 3번 북쪽 - 4번
# 12345....로 이루어진 문자열이 주어지면
# 각각의 방향으로 1m씩 이동
# 위치에서 1번 방향으로 3번 움직이고 2번 방향으로 1번 움직이고 ....
# 1번방향으로 3번움직임 => 3m,우회전 으로 표현 가능
# 1m, 좌회전 으로 표현가능 ,6m,좌회전 으로 표현가능
# 같은 방향끼리 일단 묶어주면된다  => 그러면 몇초에 어디로 이동했는지 바로 알 수 있따
# 111211111334444
# 구현

import sys
si = sys.stdin.readline
arr = si().strip()
n = len(arr)
groups = []
for i in range(n):
    if i == 0 or arr[i] != arr[i - 1]:  # 첫 문자 혹은, 이전과 다른 문자라면 즉 같은 문자끼리 연속한것을 묶어버린다
        groups.append([arr[i], 1])  # (방향, 개수)  # 연속한 같은숫자는 방향이 같고 갯수를 센다
    else: # 방향이 다르다면 바로 직전그룹과 이어지고있으므로 갯수를 증가시켜준다
        groups[-1][1] += 1
# 1. 방송하는 시간 계산
def get_announce_time(elapsed: int, length: int) -> int:
    # 이미 elapsed만큼의 시간이 지난 상태에서, length만큼 직진할 계획
    if length <= 5: # 길이가 5보다 길다 작자로 판단
        return elapsed # 바로 방송한다
    else: # 크다면 현재시간에서 얼마만큼더가야 방송을 하냐
        return elapsed + length - 5
# 2. 회전 방향 계산
def get_rotate_direction(cur: chr, nxt: chr) -> chr:
    # cur 방향에서 nxt 방향으로 바꾸려면 'left' or 'right'?
    right_rotate = { # 오른쪽 방향만 정해주면 왼쪽방향은 반대이므로 이렇게 오른쪽방향만 정해준다
        '1': '2',
        '2': '3',
        '3': '4',
        '4': '1',
    }
    return 'right' if nxt == right_rotate[cur] else 'left'
elapsed = 0 # 얼마만큼 시간이 지났느냐...
for i in range(len(groups) - 1): # 마지막은 어차피 방향지시를 할필요가없으므로 뺀다
    cur_dir, length = groups[i]
    nxt_dir, _ = groups[i + 1]
    announce_time = get_announce_time(elapsed, length)
    print(elapsed,' ',length)
    rotate_direction = get_rotate_direction(cur_dir, nxt_dir)
    print(f'{announce_time} {length if length <= 5 else 5}m {rotate_direction}')
    elapsed += length
