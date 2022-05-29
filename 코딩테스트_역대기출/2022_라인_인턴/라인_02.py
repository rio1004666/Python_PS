# n개의 줄이 필요하다
# 정확히 n개가 필요하다
# 1개에서 n개로 가기위해 k개의 줄을 선택해서
# 2k개의 줄로 복사하는 것이다 => 걸리는 시간이 k값에 따라 달라진다
# 처음에는 줄이 하나이고 이 1개의 줄을 자르기 위해 2초가 걸리고
# 두개의 줄을 자르는데 필요한 시간은 3초가 걸린다고 하자
# 그러한 n개로 되게하기 위해 자르는 방법의 수중 최소시간이 걸리도록 0
# 하는 최소시간을 구하라
# 모든 경우의 수를 해보면 n이 2000이므로 시간초과
# 동적프로그래밍으로 접근해볼 가치가 있다
# n개의 줄을 만들기 위해 마지막에 몇개의 줄을 복사했느냐가 관건
# 10개의 줄을 만들고 싶다 => 다양한 시나리오가 있겠지만
# 공통점은 마지막에 한줄만 잘라서 나온것이 있고 두개줄을 자랄서 나온것이 있을것이다
# 마지막에 한개를 잘랐을 경우 최소시간을 저장하고
# 마지막에 두개를 잘랐을 경우 최소시간을 저장하고....
# 이 중 작은 것만 선택하면 된다
# 각각의 파티션을 빠르게 구하자 ( 마지막 결과만을 나눈것들 )
# dp[i] = 정확히 i개가 되는 최소 시간
# 테이블 정의 => n개의 줄을 구하는데 걸리는 최소시간
# dp[n]에 저장
# 초깃값은 이미 1개일때는 0초의 시간으로 만들수있는것이다
# 정답 구하는 방법 확인
# dp[i] = k개의 줄을 선택해서 Tk 계산.... k개의 줄이 2k로 복제가 되고 i가된다
# 1->i-k까지 복제가 되고 여기서 i가 됨
# Tk = dp[i-k] + times[k] => 4줄이 되기위해서는
# dp[3] 은 3줄상태에서 1줄을 자르면 4줄이 되므로 dp[3] + times[1]이 가능하다 dp[3]은 이전에 3줄상태에서 최솟값상태가 저장되므로 불러오기만 하면되므로 다이내믹 프로그래밍이 가능하다
# dp[2] 은 2줄상태에서 2줄을 자르면 4줄이 되므로 dp[2] + times[2]이 가능하다 dp[2]는 이전에 2줄상태에서 최솟값상태가 저장되므로 불러오기만 하면되므로 다이내믹 프로그래밍이다
# dp[1] + times[3] 1줄 상태에서 3개를 자를 수 없으므로 패스한다
#  dp 파라미터를 1개냐 2개냐로 따져본다 1개로 할 수 있으면한다 우선
# dp 테이블 정의서를 세우자  구하고자하는 값을 명확히하고 파라미터를 정하자 1개가 될지 두개가 될지
# 모든 dp 문제는 테이블 정의와 점화실을 세우면 끝이다 # 그 다음 조건에 따라 설정해주고 최소 최대를 구해주면 된다

import sys

si = sys.stdin.readline
n = int(si())
times = [0] + list(map(int, si().split()))
dy = [0 for _ in range(n + 1)]
dy[1] = 0
for i in range(2, n + 1): # 2줄 만들고 싶은 경우
    # dy[i] 계산을 하고 싶은 상황
    res = -1
    for k in range(1, i + 1): # 1개 자르거나 2개를 자를 수 잇다
        # 마지막에 k 개를 복제한 상황에 대한 부분 정답 계산
        if i - k < k: # 4개를 만들고 싶은데 1개를 자르는것 2개를 자르는것까지는 가능 3개를 자르는것은 불가 => 4개로 만들 수 없음
            break
        # i-k즉 자르기 전의 파라미터값을 메모이제이션 한다
        val = dy[i - k] + times[k] # 4개를 자르기 위해서 3개에서 1개를 자르면 4개가 되고 4개를 만들기 위해서 2개를 2개로 자르면 4개가 된다 1개를 3개로 자를수없음 4개 이상이되므로 더이상 할 필요가 없다
        if k == 1: res = val # 처음 한개를 잘랐을경우 값을 초기값으로 셋팅한다
        res = min(res, val) # 그다음 계속 값을 갱신한다
    dy[i] = res

print(dy[n])