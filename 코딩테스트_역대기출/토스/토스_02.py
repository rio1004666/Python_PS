# 바구니가 있다
# 바구니는 최대 W 만큼의 무게를 감당할 수 있다
# 가지고 있는 사과가 여러개 있다
# 사과가 총 N개 있다
# 각 사과마다 무게가 다르다
# l1 , l2, l3, l4.... 이 사과들을 전부 바구니 안에 담고싶은데
# 바구니는 최소 몇개를 필요로하는지 궁금하다
# 최대 20만큼 감당할 수 있는 바구니
# 들고 있는 사과가 7개
# 각각 무게가 1 2 2 18 18 18 18 이 있다
# 얘내들을 모두 바구니에 담기 위해 필요한 바구니 수는
# 4개가 된다 즉 정답이 4가 된다
# w는 40 n의 범위는 12개이다
# 모든 사과를 담을 수 경우의 수가 없으면 -1을 반환
# 각 사과의 무게도 최대 40까지 가능
# 생각하는 방법 이 문제를 읽고
# 이게 좀 특이한데?
# 이게 문제풀이에 도움이되고 접근법에 도움될거같은데?
# 키워드! => N제한 크면 시간복잡도 유의 => 엄청 작아도 힌트가 됨 => 브루트포스인가
# 12밖에 안되기 때문에
# 완탐으로 가능 할 수 있다
# N개의 사과를 만들고
# 바구니 집합을 만든다
# 맨 처음에는 아무런 바구니가 없다
# 매 사과마다 어떤 선택을 할거냐면
# 이미 잇는 바구니에 넣거나 새로운 바구이를 만들어서 넣거나
# 이 두가지의 선택중 하나를 선택해서
# 재귀호출할 것이다
import sys
si = sys.stdin.readline
N,W = map(int,si().split())
a = list(map(int,si().split()))
ans = N
if max(a) > W: # 한 바구니에 담을 수 없는 사과가 있으면 아웃
    print(-1)
    exit()
def backtracking(idx, buckets):
    global ans
    if idx == N:
        ans = min(ans, len(buckets))
        return
    # branching 가지치기 테크닉
    if ans <= len(buckets): # 모든 사과를 담지 않앗는데도 불구하고 더이상 완탐할 가치가 없으므로 돌아간다
        return
    # 기존 바구니가 있다면 담아본다 담을 수 없다면 새로운 바구니를 생성해서 담는다
    for bucket_idex in range(len(buckets)):
        if buckets[bucket_idex] + a[idx] <= W:
            buckets[bucket_idex] += a[idx]
            backtracking(idx+1,buckets)
            buckets[bucket_idex] -= a[idx]
    # 위에서 기존의 바구니에 담을 수 없는경우 새로운 바구니를 생성하여 담는다
    buckets.append(a[idx])
    backtracking(idx+1,buckets)
    buckets.pop()
backtracking(0, []) # 0번인덱스부터 시작하고 바구니는 하나도 없어
print(ans)