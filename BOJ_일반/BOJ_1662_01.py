# 여기서 키포인트는 숫자 ( ) 이 세가지유형만 들어온다고 했으므로
# 이거에 따라 처리해야함을 알 수 잇다
import sys
si = sys.stdin.readline

S = si()

stack = []
length = 0
temp = ''
for c in S:

    if c.isdigit():
        length += 1
        temp = c
    elif c == '(':
        # 기억해놓아야 할 정보는 가공된 데이터이다
        stack.append((temp, length - 1)) # 숫자는 이전에 저장되어 있다 곱할 숫자가
        length = 0 # 길이 초기화 후 다음 길이 구할때 사용
    elif c == ')':
        multiply, preL = stack.pop()
        length = (int(multiply) * length) + preL

print(length)
