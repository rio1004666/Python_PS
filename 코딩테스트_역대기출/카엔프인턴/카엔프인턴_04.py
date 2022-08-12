# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


# 우선 문자열을 리스트로 담아서 변형시켜야겟네

import sys
si = sys.stdin.readline
N = int(si())
s = si()
p = ''
for i in range(N):
	if 'a' <= s[i] <= 'z':
		p += s[i]
print(p)
arr = [i for i in s.rstrip()] # 문자열을 리스트로 변환
answer = ''
# 우선은 과장된 소문 만들기
for i in range(len(s)):

	if ord(s[i]) + (i+1) > 122:
		plus = ord('z') - ord(s[i]) + 1
		addition = (i+1) - plus
		addition %= 26
		answer += chr(ord('a') + addition)
	else:
		answer += chr(ord(s[i]) + (i+1))
# 이제 원래소문과 과장된 소문 한자리씩 비교해가면서 알바펫순으로 순서상 앞에 있다면 없어짐
print(len(answer))
print(len(s))
if len(answer) > len(s):
	answer2 = ''
	for i in range(len(s)):
		answer2 += answer[i]
else:
	print(answer)

