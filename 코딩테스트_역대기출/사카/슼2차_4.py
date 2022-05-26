4.
# 8 4 4 2
# 1 5 1 3
# 5 7 5 6
# => 1 3 1 2
# 8 4 4 1
# 1 5 1 3
# => 1 4 1 3
# 10 3 3 2
# 1 2 3
# 5 7 10
# => 1 2 3

# N개의 칸중에서 U개의 칸을 고름
# N이 7이고 U가 4면 7개중 4개를 고름
# 마음속에 P자리 비밀번호가 있고
# 1부터 U(used)사이의 숫자로만 이루어져 있다
# U가 4면 P는 1부터 4까지 P자리 비밀번호로 이루어짐
# 왼쪽부터 차례로 1,2,3,4 가 적혀짐
# P자리 비밀번호 3 1 4 3 이라면
# 3이 가리키는 위치인 5를 누르고
# 1이 가리키는 위치인 2를 누르고
# 4가 가리키는 위치인 7를 누르고
# 3이 가리키는 위치인 5를 누른다
# 그럼 비밀번호가 5275로 형성된다
# 이러한 방식으로 여러개 형성되면 원래 비밀번호를 유추하는 문제
# 사용한 숫자들중에 사전순으로 가장 큰것을 출력

# 다시 이해한것을 정의해보자
# 그러니까 기록들 즉 눌러진 비밀번호들을 보고
# 원래비밀번호를 유추해야한다
# 단 크기순으로 알맞게 되어있어야한다



import sys
si = sys.stdin.readline
N, U, K, R = map(int, si().split())
maxgap = [N + 1 for _ in range(N)]          # maxgap[i] := i번째로 작은 수와 i-1번째로 작은 수의 차이의 상한
password_number_cnt = 0
# ---------------------------------------
# O(R * K * log (K))   R <= 1,000, K <= 5,000
for _ in range(R):
    record = list(map(int, si().split()))   # 기록 입력
    use = sorted(list(set(record)))         # 사용한 위치 중복 제거 + 정렬
    password_number_cnt = len(use)          # 실제 비밀번호가 몇 개의 수로 이루어져 있는 지 세기
    for i in range(password_number_cnt):
        gap = use[i]                        # 인접한 차이 계산하기
        if i > 0: gap -= use[i - 1]
        maxgap[i] = min(maxgap[i], gap)     # i번째로 작은 수와 i-1번째로 작은 수의 차이의 상한이 gap
# ---------------------------------------
presum = maxgap                             # 차이를 가지고 복원한 실제 사용된 비밀번호의 수들
for i in range(1, password_number_cnt):
    presum[i] += presum[i - 1]
for i in range(password_number_cnt):        # U 라는 상한에 의해 생기는 제한 적용
    presum[i] = min(presum[i], U - (password_number_cnt - 1 - i))
convert = [0 for _ in range(N + 1)]         # convert[x] 는 x번 칸에 실제로 써있던 비밀번호
for i in range(password_number_cnt):
    convert[use[i]] = presum[i]
for x in record:
    print(convert[x], end=' ')              # 실제 비밀번호 복원하는 과정