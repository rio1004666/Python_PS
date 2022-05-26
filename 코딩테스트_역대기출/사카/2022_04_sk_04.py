# A라는 배열을 B라는 배열로 만들고 싶다
# 4 2 3 1 7 1... (A배열)
# B배열을 어떻게 만드냐
# B[i]는 i의 약수인 모든 j의 A[j]의 총합
# B배열을 구하라! N제한 20만
# NlogN 혹은 NrootN이다
# B를 하나씩 구하는것보다는 A하나를 가지고
# B어디에 누적되는지 구하면된다 (반대로 생각하기)
# A[3] 즉 7이 써저있다면 B 어디에 영향줄지 생각해보면
# B의 3배수에 전부 들어가줘서 더해준다
# 에라토스테네스의 체와 유사
# 소수판별시 모든 배수에 체크해서 아닌것만 선별
# 어떤 수의 약수를 다찾는건 어렵고
# 어떤수의 배수를 찾는건 쉽다
# 시간복잡도 계산
# N/1 + N/2 + N/3 + .....
# N(1/1+1/2+1/3+1/4+.....)
# N(logN)


import sys

si = sys.stdin.readline
n = int(si())
a = [0] + list(map(int, si().split()))
b = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        b[j] += a[i]

for i in range(1, n + 1):
    print(b[i], end=' ')