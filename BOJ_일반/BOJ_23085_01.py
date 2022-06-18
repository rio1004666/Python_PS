# 임의의 동전을 뒤집어서 현재 상태의 동전을 전부 뒷면으로 바꾸기 위한 최소 횟수 => 최소가 들어가면 다익스트라 BFS 이분탐색 등
# 이분탐색은 아니다 우선 ( 반대로 정답을 미리 정해보고 이게 최소가 되는지 답을 넣어보는 류가 아니다 )
# 상태의 변화에 따른 최소횟수이기때문에 그래프문제로 해석될 수 잇따 => BFS
# 이문제에서 핵심은 임의의 동전을 뒤집어본다이기때문에 순서를 생각하지 않으므로 DFS로 가는것이 아닌
# 갯수만 생각하면 된다 임의 뒷면을 1개 뒤집으면 K-1개 앞면을 뒤집으면된다 즉 내가 선택하는 것이 아닌 갯수만 생각하면 되는 것이다
import sys
from collections import deque
si = sys.stdin.readline
N,K  = map(int, si().rstrip().split())
coin = si()
back_cnt = 0 # 뒷면의 갯수를 알면 나머지는 앞면의 갯수를 알고 이것을 알아야 몇개를 뒤집는것이 가능한지 알 수 있다
def bfs(back_cnt):
    visited = [False]*(N+1)
    q = deque([(back_cnt,0)])
    visited[back_cnt] = True # 뒷면의 갯수가 이미 카운팅 됫다면 더이상 카운팅하지 진행하지 않는다
    while q:
        turn_back_cnt, k_turn_cnt = q.popleft()
        turn_front_cnt = N - turn_back_cnt
        # 인접한 노드 즉 상태들을 전부 생각해준다 뒷면 0개면 앞면은 K개 뒷면 1개면 앞면은 K-1개 ..
        # 전부 현재의 상태를 뒤집어본다는 브루트 포스 ( 인접한 상태를 )
        for i in range(K+1): # 0개부터 k개까지 뒵지어본다 즉 앞면 뒷면 균형을 이뤄서 뒤집어볼것이다
            turn_back = i # 뒷면을 뒤집을 갯수
            turn_front = K-i # 앞면을 뒤집을 갯수
            # 뒤집힐 갯수보다 뒤집을 갯수가 많을 수는 없으므로 이 경우는 패스한다
            # 가지치기 => 효율성
            if turn_back > turn_back_cnt or turn_front > turn_front_cnt:
                continue
            back_cnt = turn_back_cnt-turn_back + turn_front # 뒤집혀있는것을 뒤집으면 앞면이되므로 그 개숫만큼 빼주고 앞면은 뒷면이 되므로 더해준다
            if back_cnt == N:
                return k_turn_cnt + 1
            if visited[back_cnt]: # 그리고 뒷면의 갯수를 이미 방문한적이 있다면 더이상 방문할 필요가 없다 ( 최소가 되기 위한 )
                continue
            # 방문한곳 제외 => 효율성
            visited[back_cnt] = True
            q.append((back_cnt,k_turn_cnt + 1))
    return -1 # 결국 위의 과정을 거쳤음에도 모두 뒷면이 될 수 없는 상태라면 -1을 반환한다
for i in range(N):
    if coin[i] == 'T':
        back_cnt += 1
if back_cnt == N:
    print(0)
else:
    answer  = bfs(back_cnt)
    print(answer)