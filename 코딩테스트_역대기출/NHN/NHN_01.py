# 524136 (카드 배열 )
# 1번연산 : 반으로 쪼개서 앞의 반을 뒤의 반 뒤에 붙여서 배열을 만든다
# 2번연산 : 반으로 쪼개서 뒤의반부터 한장씩 깔고 그다음 앞의 반 앞장을 깔고 해서 섞는다
# N제한 1000 (카드수) M제한 10000 ( 쿼리 )
# 범위가 이상하다 시간복잡도 계산..1억 1초 가정
# 1억을 넘든 경우가 많다 .....
# 1번연산 함수 2번연산 함수 만드는 것이 핵심
import sys

si = sys.stdin.readline
N,Q = map(int, si().split())
a = list(map(int,si().split()))
def A(a: list) -> list:
    return arr[N//2:] + A[:N//2]
def B(a: list) -> list:
    ret = []
    for x,y in zip(arr[:N//2],arr[N//2:]):
        ret.extent([x,y])
    return ret
for _ in range(n):
    query = si().strip()
    if query == 'A':
        arr = A(arr)
    else:
        arr = B(arr)
