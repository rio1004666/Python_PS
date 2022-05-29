# N개의 문자열들이 주어짐
# 사람이름 음식이름
#  ryu      apple
#  ryu      banana
#  ho        apple
# seok       pear
# 가장 인기 있는 음식을 알고 싶다
# 인기 음식이란 절반이상의 사람이 좋아하는 음식을 의미
# apple을 좋아하는 사람이 ryu와 ho라는 2사람이 전체 사람 3명중 과반수이상이 좋아하므로
# apple만을 출력한다

import sys
from collections import defaultdict
si = sys.stdin.readline
n = int(si())
names = set()
fruits = defaultdict(int)
for _ in range(n):
    name, fruit = si().split()
    names.add(name)
    fruits[fruit] += 1
ans = list()
threshold = (len(names) + 1) // 2
for fruit, cnt in fruits.items():
    if cnt >= threshold:
        ans.append(fruit)
ans.sort()
print(len(ans))
print(*ans)