"""
이베이코리아 5번 블라썸 알고리즘(최대 매칭 알고리즘)
# 완전탐색으로도 할 수 있다 (블라썸 알고리즘도 잇지만 잘모르면)
"""

def solution(P):
    length = len(P)
    visited = [-1] * length
    ans = [0] * length
    pos = [[0 for _ in range(length)] for _ in range(length)]
    def preprocess():
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                # 만약 i랑 j매칭가능?
                pal = P[i] + P[j]
                if pal == pal[::-1]:
                    pos[i][j] = 1
                    pos[j][i] = 1
    def dfs(idx, visited, cnt):
        nonlocal ans
        # 가지치기 한다
        if visited[0] != -1 and ans[visited[0]] == 1:
            return
        if cnt == 0: # 모두 매칭이 되는 순간에
            ans[visited[0]] = 1 # 0번과 매칭되는 놈을 출력...?
            return  # 모두 매칭되는 것을 다 찾아봄으로....
        # 0번이 5번 매칭해봣으면 다음에 또 매칭할 필요?
        # 한번 매칭 성공했다면 5번은 다시 0번과 매칭할 필요가 없다 
        if idx > length:
            return
        if visited[idx] != -1:
            dfs(idx + 1, visited, cnt)
        for i in range(idx + 1, length):
            if visited[i] == -1:
                # 두개를 그대로 붙이거나 바꿔서 붙여서 팰린드롬이면 붙여본다
                # idx = 5 , i = 10
                # 짝을 이룰수있냐 확인하는 시간이 때때로 오래걸릴수잇다
                # 언제? 문자열이 길면 매번 이렇게 붙일것이다
                # 그래서 한번 매칭해놓고 가져다 쓰기만 하면 상당히 시간을 절약할 수 있다
                # 그래서 판단을 매번해야하는 경우는 미리 판단을 해놓고 가져오는 것이 좋다
                # pal = P[idx] + P[i]
                # repal = P[i] + P[idx]
                # 그런데 이 팰린드롬 판단행위를 미리 해놓으면
                # 그걸 가져오기만 하므로 훨씬 복잡도가 줄어든다
                #if pal == pal[::-1] or repal == repal[::-1]:
                if pos[idx][i] == 1:
                    visited[idx] = i
                    visited[i] = idx
                    dfs(idx + 1, visited, cnt-2)
                    visited[i] = -1
                    visited[idx] = -1
    preprocess()
    dfs(0, visited, length)
    # 리스트 컴프리핸션 잘 사용하자
    return [P[i] for i in range(length) if ans[i]]

#print(solution(["21","123","111","11"]))
# 1이 만약 20개라면 나머지 19개의 1이 나와야한다
# 근데 너무 오래걸린다 매칭 될 수 있는 모든 경우의수를 다해봄으로
# 이미 매칭해봣던 애들은 거른다.
print(solution(["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]))




