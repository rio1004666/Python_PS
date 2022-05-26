import re

# 문자열 원소 접근
a ="hello"
print(a[0]) # 문자열 접근
# 문자열 슬라이싱
a="apple"
b = a[1:3]
print(b)
print(a[:4])
print(a[2:])
for s in a:
    print(s)
print(a+b)
# 문자열 반복

c = '모두 "안녕"이라 인사해요'
print(c)
c = '모두 \"안녕\"이라 인사해요'
print(c)
d = c.find('안녕')
print(d)
# 문자열 바꾸기
e = c.replace("안녕","방가")
print(e)
# 문자열 나누기
g = c.split()
print(g)
k = 'ArrTYfghn'
temp = k.upper()
print(temp)
temp = k.lower()
print(temp)

temp = re.findall('[a-z]', k) # 알파벳 소문자만 추출하기
temp2 = ''.join(temp)
print(temp2)
print('==========  숫자만추출하기')
aa = 'greger12432'
digits = re.sub(r'[^0-9]','', aa)
print(digits)
