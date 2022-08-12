answer = 0


def dfs(cnt, k, dungeons, visited):
    global answer
    # 마지막 던전이거나 최소 필요도를 충족하지 못했을 경우 최댓값을 갱신하고 빠져나온다

    if answer < cnt:  # 방문한 던전방 갯수가 업데이트 됨
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:  # 방문하지 않았고 방문할 수 있는 최소 필요도가 충족되면
            visited[i] = True
            dfs(cnt + 1, k - dungeons[i][1], dungeons, visited)  # 파라미터로 넘겨주기만 하면 굳이 계산할 필요가 없음 => 원복시킬 필요가 없어짐
            visited[i] = False  # 다시 백트래킹함


def solution(k, dungeons):
    # 동굴 탐험 순서를 바꾸면된다 8! = 40320 => 완전 탐색 ( 동굴 8개뿐)
    # 최소 필요 피로도가 충족되지 않으면 빠꾸
    visited = [False for _ in range(len(dungeons))]
    dfs(0, k, dungeons, visited)
    return answer