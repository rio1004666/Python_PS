# 내 풀이
# def solution(a,b):
#     answer = 0
#     n = len(a)
#     for i in range(n):
#         answer += a[i]*b[i]
# 다른 사람 풀이 => 파이썬은  list comprehension으로 바로 sum함수를 사용할 수 있다
# zip 은 두개의 배열 각 원소를 튜플형태로 받을 수 있다

def solution(a,b):
    return sum([x*y for x,y in zip(a,b)])

print(solution([1,2,3,4],[-3,-1,0,2]))