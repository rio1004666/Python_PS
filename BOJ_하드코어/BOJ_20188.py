# 각각의 간선 N-1개가 얼마나 사용되는지 알려면,
#
# 트리를 dfs로 각 간선을 돌면서 각 경우의 parent 노드를 포함한 서브트리의 크기를 제외한 경우의수를 구해주면 된다.


import sys

sys.setrecursionlimit(309999)

N_ = int(sys.stdin.readline())
grp_ = [[] for _ in range(N_ + 1)]
for _ in range(N_ - 1):
    a_, b_ = map(int, sys.stdin.readline().split())
    grp_[a_].append(b_)
    grp_[b_].append(a_)

lst_c = [0 for _ in range(N_ + 1)]
ans_ = 0
cch_ = (N_ * (N_ - 1)) // 2


def nc2_(n_):
    return (n_ * (n_ - 1)) // 2


def func_(idx_):
    global ans_, cch_
    lst_c[idx_] = 1
    for idx_c in grp_[idx_]:
        if not lst_c[idx_c]:
            lst_c[idx_] += func_(idx_c)
    ans_ += cch_ - nc2_(N_ - lst_c[idx_])
    return lst_c[idx_]


func_(1)
print(ans_ - cch_)
print(lst_c)
exit()