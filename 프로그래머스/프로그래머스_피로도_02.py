
def dfs(cnt,k,dungeons,visited,answer):

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            answer = dfs(cnt+1, k-dungeons[i][1],dungeons,visited,answer)
            visited[i] = False
    # 리턴값을 저장하는 dfs형식 => 모든 던전을 순회후 최종 방문 던전수를 갱신한다
    answer = max(answer,cnt)
    return answer

def solution(k,dungeons):
    answer = 0
    visited = [False for _ in range(dungeons)]
    dfs(0, k, dungeons, visited, answer)
    return answer