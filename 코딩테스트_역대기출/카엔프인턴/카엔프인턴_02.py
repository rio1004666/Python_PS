# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

import sys

si = sys.stdin.readline

N = int(si())
s = si()
new_digit = {}
# 하드코딩해야만 함 여기서는
new_digit['qw'] = '1'
new_digit['as'] = '2'
new_digit['zx'] = '3'
new_digit['we'] = '4'
new_digit['sd'] = '5'
new_digit['xc'] = '6'
new_digit['er'] = '7'
new_digit['df'] = '8'
new_digit['cv'] = '9'
new_digit['ze'] = '0'

# 하나씩 체크해보면서 두자맀기 새로운숫자 사전에 있는지 확인만 하면 되고 있으면 정답문자열에 추가하면 끝
answer = ''
for i in range(len(s) - 1):
    temp = ''
    temp += s[i]
    temp += s[i + 1]
    if temp in new_digit:
        answer += new_digit[temp]

print(answer)


