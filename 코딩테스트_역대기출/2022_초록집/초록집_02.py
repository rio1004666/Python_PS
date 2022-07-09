# 쇼핑몰 여러가지 제품
# G개 등급 존재
# G가 5라면 A~E까지 존재
# 쇼핑몰에서 설문을 받음
# 상품이름 등급 형태로 평가해서 설문작성함
# apple A 이런 형식으로 매김
# 등급은 A가 제일 높은 등급
# 설문지들이 여러개 있을 것임
# 한 제품에 등급이 여러개 매겨질것임
# apple 제품에 A등급 2 B등급 6 C 등급 4 D등급 6
# apple의 메인 등급은 제일 많이 받은 등급이 메인등급
# B등급이 제일 많이 받음
# 다른 등급들도 정렬 가능함
# 많은 투표를 받은 등급일 수 록 더 높은 평가가 됨
# BDCA 순으로 등급을 매김
# 결론저긍로 하고 싶은것은
# 각 등급별로 속한 상품을 출력
# 메인 등급에 속한 상품들을 출력
# 같은 등급에 여러개의 상품이 있다면
# 그 다음 두번째 높은 등급으로 정렬함
# 또 두번째가 같은 등급이라면 그 다음 세번째 등급을 비교함
# 여기서 포인트는 같은 등급이면 다음 차순 등급 비교를
# 튜플이나 리스트로 묶어서 정렬 시키면
# 알아서 정렬되고 해당 상품의 등급 평가가 없다면 메인등급을 매기고
# 정렬시키면 된다
# 혹은 문자열로 전환후 정렬하면 차례로 정렬시킨다
# 상품별 등급별 횟수 기록 자료구조 필요
# 상품 구별 기준이 문자이기 때문에 딕셔너리 사용
# 그리고 상품이 받은 등급의 갯수가 많은 순으로 내림차순 정렬한 상태에서
# 등급이 매겨져 있어야 한다
import sys
from collections import defaultdict
from functools import cmp_to_key # 정렬 기준을 세우기 위함임
si = sys.stdin.readline
G, num_survey = map(int, si().split()) # 등급의 갯수와 설문 수를 입력받고
mem = defaultdict(dict) # 이중 딕셔너리 사용한다
for _ in range(num_survey): # 설문지 내용을 입력받는다
    name, grade = si().split()
    if grade not in mem[name]: # dict는 키가 없으면 값을 업데이트 할 수 없으므로 체크한다
        mem[name][grade] = 0
    mem[name][grade] += 1 # 키가 있다면 +1 업데이트 한다
ordered_mem = dict() # 딕셔너리 또 선언해준다 값은 리스트로 셋팅을 할것이다
for name, survey_result in mem.items():
    arr = list(survey_result.items()) # 위의 결과를 가지고 리스트로 만든다
    arr.sort(key=lambda x: (-x[1], x[0])) # 가장 많이 받은 등급순으로 정렬하고 같으면 사전순으로 정렬한다
    ordered_mem[name] = [v[0] for v in arr] # 메인등급을 가져온다
grades = dict()
for i in range(G):
    grades[chr(i + ord('A'))] = []  # 각 등급은 대문자 알파벳이므로 그냥 알파벳을 키로 가져오고 상품들을 리스트로 값을 정한다
for name, arr in ordered_mem.items(): # 정렬된 상품별 등급목록을 가져와서
    grades[arr[0]].append(name) # 그 등급에 해당하는 상품이름을 기록한다

def compare(A, B): # 우선순위를 함수로 정의해서 정렬함
    # 만약 A 가 B 보다 우선순위가 높다면 False, 아니면 True를 돌려주는 함수
    # 이미 ordered_mem으로 정의를 정렬해놓은 기록이 있으므로 이것들로 비교한다
    # 정렬기준을 다른 자료구조에서 가져와도된다 꼭 정렬할 자료구조에서 가져오는것은 아니다
    # 길이가 다르면 더 큰것으로 선택해서 반복해서 없는것은 메인등급으로 매기는 방식으로 진행함
    lenA = len(ordered_mem[A])
    lenB = len(ordered_mem[B])
    # 상품하나하나씩 체크해서 우선순위를 정한다 정해질때까지
    for i in range(max(lenA, lenB)): # 받은 등급의 갯수가 다를 수 있다 즉  A나 B 둘중에 받은 등급의 갯수가 작은 상품이 있다면 등급을 못받은 제품의 나머지 등급은 메인등급으로 취급하여 비교한다

        if i < lenA:
            vA = ordered_mem[A][i]
        else:
            vA = ordered_mem[A][0]

        if i < lenB:
            vB = ordered_mem[B][i]
        else:
            vB = ordered_mem[B][0]
        # 최종적으로 비교한다 작은것은 -1 큰것은 1을 반환하면 된다 또 모든 등급을 비교해서 같다면 상품이름 알파벳순으로 비교한다
        if vA < vB: return -1
        if vA > vB: return 1
    # 전부 다 비교해도 같다면 결국 이름 사전순으로 비교할것이다 여기서 1을 때리면 큰 값이 나오므로 마지막에 이름을 비교해준다
    return 1 if A > B else -1 # 파이썬의 삼항 연산자
    # 결국 -1이냐 1이냐로 결정되기 삼항연산자로 처리해준다 문자열 비교는 단순 앞에서부터 알파벳 사전순으로 비교하게 된다


for g, names in grades.items():
    # 해설은 크기가 크지 않기때문에 선택정렬을 사용하였다
    # for i in range(len(names)):
    #     for j in range(i + 1, len(names)):
    #         if compare(names[i], names[j]):
    #             names[i], names[j] = names[j], names[i]
    # 그런데 sort사용하는 것이 역시 좋것지?
    # 문제는 알파벳순으로 정렬하지 않게 된다
    names.sort(key=cmp_to_key(compare))
    if names:
        print(*names)
    else:
        print('-')
# 4 6
# grape B
# banana B
# banana B
# grape B
# grape A
# banana A