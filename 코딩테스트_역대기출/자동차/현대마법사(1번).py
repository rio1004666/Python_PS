
"""
<<  시뮬레이션  >>

이진수 말장난 문제
이진수가 주어지면 B0 = 11100011010   K번 변환할것이다 => 그룹으로 모은다
                       각 그룹별로 갯수를 구한다
                        3  3  2 1 1 1 => 2진수로 바꾼다 => 이어준다
                        11 11 10 1 1 1 => 111110111
                        다시 => 각 그룹으로 모아서 갯수를 센다
                        513=> 2진수로 바꾼다 101 1 11
                        101111 =>다시 그룹으로 모은다
                        104 => 다시 2진수로 바꾼다

시뮬레이션=> 항상 손으로 먼저 짜본다
그룹으로 갯수를 변환하다 T(B) 라는 함수를 만든다 => Binary String B를 변환 결과
다시 2진수로 변환하는 함수 GetBinary(x:int) -> str: 정수를 받아서 문자열을 반환한다

"""



import sys
si = sys.stdin.readline
Binary, K = si().split()
K = int(K)
def GetBinary(x: int) -> str:
    res = ""
    if x == 0:
        return '0'
    bins = ['0', '1']
    while x > 0:
        res = bins[x % 2] + res
        x = x // 2
    return res

def T(B: str) -> str:
    counts = []
    last = -1
    for ch in B:
        if ch == last: # 마지막문자가 현재문자와 같다면 +1해준다
            counts[-1] += 1
        else: # 그게 아니라는 것은 새로운 숫자가 등장했을 경우 그냥 1로 추가한다
            counts.append(1)
            last = ch
    return ''.join(map(GetBinary, counts)) # 리스트에 있는 원소들을 map함수로 적용한다
for _ in range(K): # k번 실행이다
    Binary = T(Binary)
print(Binary)