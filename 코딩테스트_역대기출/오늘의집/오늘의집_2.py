
# 최빈값 => 가장 빈도수가 높은 수
# 최빈 부분 문자열 => 찾고 그걸 다 지운다
# 연속한 문자열  => 부분 문자열 => 가장 많이 나타나는 문자열
# 대소문자 가리지 않음
# 어떤 문자열 => 임의 문자열 => 등장횟수 계산
# 키가 문자열이고 value가 숫자인 key,value 자료구조 => dict()
# D[str] = str이 부분문자열로 등장하는 횟수
# 부분문자열을 i,j로 설정 substr 가지고 D라는 자료구조 완성
# 이 과정에서 최빈등장횟수도 계산
# 최빈등장횟수 K라고 했을 경우 문자열에서 지워주는 작업
# abcabcdefabc => 3번 등장하는게 제일 많은 빈도수다
# erase 배열 만들어서 false로 마킹해놧다가 지워지면 true로 체크해준다
# 모든 부분문자열을 다확인하므로 완전탐색에 속함

# n제한 1000
# 2 - n^3 코드 => 시간초과날수있으므로 n^2으로 하게 해야한다 최적화해서

import copy
from collections import defaultdict
from re import sub
import sys
si = sys.stdin.readline
str = si().strip()
copied_str = copy.deepcopy(str) # 참조하지 않는 독립된 배열 따로 생성
# copy.deepcopy 로 원래 문자열을 저장해놓음
str = str.lower() # 소문자처리 ( 변경되버리므로 원래문자열 백업후 변경 )
n = len(str)
D = defaultdict(int) # value값으로 0을 디폴트설정
max_value = 0 # 최빈도 저장하는 변수
for i in range(n):
    substr = ""
    for j in range(i, n): # 모든 부분문자열을 딕셔너리에 박음
        substr += str[j] # 리스트에서 빼오는것보다 시간이 더짧아질것이다
        D[substr] += 1
        max_value = max(max_value, D[substr]) # 여기까지가 100만

erased = [0 for _ in range(n)]
for i in range(n):
    substr = ""
    for j in range(i, n):
        substr += str[j]
        if D[substr] == max_value:
            for k in range(i, j + 1): # 이게 구리다 erased하는 것을.......
                erased[k] = 1
for i in range(n):
    if erased[i] == 0:
        print(copied_str[i], end='')


# 관찰하자!!!!  abc 3번등장=> abc의 부분문자열 ab도 3번 등장
# 즉 ab는 최빈도수가 3이상이다 항상
# 최빈부분문자열 = 길이 최소 1 것만봐도 부분문자열 최빈을 알수잇다
# 즉 가장 많이 등장하는 알파벳 다지우자자
# ad-hoc 이라고 볼수있다 (완탐보다 훨씬 성능 개선)
# 또 ab의 부분문자열 a와 b와 c는 3번등장한다
# 결론 : 가장 많이 등장하는 알파벳을 다지우자
# 최소 abc 가 3번등장하고 a와 b와 c는 각각 3번은 무조건 보장하고
# 또 다른위치에서 만약 a혹은 b혹은 c가 혼자서 나타난다면
# 최빈수가 3번 초과가된다 무조건 연속한문자갯수가 1개인것만 많이 나타나는
# 최빈값으로 보자는 것이다
# 최빈부분문자열은 즉 길이가 1인 문자열이다!!!
# 2 - 정해



si = sys.stdin.readline
str = si().strip()
copied_str = copy.deepcopy(str)
str = str.lower()
n = len(str)
count_alphabet = [0 for _ in range(26)]
for c in str:
    count_alphabet[ord(c) - ord('a')] += 1
max_value = max(count_alphabet)

for (c, copied_c) in zip(str, copied_str):
    if count_alphabet[ord(c) - ord('a')] != max_value:
        print(copied_c, end='')