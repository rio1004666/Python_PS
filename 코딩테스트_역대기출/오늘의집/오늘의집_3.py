# 3.
# 문자열이 주어지고
# {}로 묶여있는것은 변수이다 => 바뀔수잇다
# 입력예제
# str이라는 변수는 -> B라는 문자로 대체되고
# abc라는 변수는 -> def로 대체된다
# str이라는 변수는 {str} 이고 B로 변환된다
# abc라는 변수는 {abc} 이고 def로 변환된다
# 템플릿이 주어지고 변수정보가 주어졌을 경우
# 변수정보를 템플리에 대입해서 결과문자를 리턴함
# 단,, 입력이 항상 제대로 들어오지 않음
# 예를들어  모든 변수는 다른 변수로 바뀔수도 있다!!!!
# str은 {abc} 변수로 바뀌고 또 {abc} 는 {def}로 바뀐다
# 그럼 결국 전부 def로 바뀌고
#  또 없는 변수로 바뀔 수 있다 .
# str -> {abcd} 로 바뀌면 그냥 abcd로 바꾸면되고
# abc -> def로 바뀌면된다
# 순환구조가 될 수도 있다  str -> {abc} -> str로 바뀔수잇으므로 해결되지 않으므로 그대로 str출력한다
# 30만개 template 10만개 => 관계 개수
# 문자열을 정점 변환관계를 간선으로 하는 그래프문제!!!로 생각해보자 => 어떤 상태가 어떤 상태로 변환되는 것들은 그래프로 생각해볼 수 잇다
# 위상정렬의 아이디어를 활용해서 풀어보자
# 변환관계가 그래프가 될 수 있따
# 먼저 해야하는것은 변수 (변하는수) 들이 문자인지 변수인지 판단을 해야한다
# 변수에서 문자로 변화는건 확정적으로 단어로 된다
# b라는 단어가 c라는 변수로 바꾼다는 판단이 될거고
# 또 c라는 변수가 단어로 바뀌는게 있는지 찾아본다 => dfs탐색
# 근데 찾아도 없다면 => 단어로 확정적으로 바꾸면된다
# 그래프 문제는 항상 정점 과 간선을 정의
# 정점은 각 문자열 변수
# 간선은 어떤 변수가 다른 변수로 변환될 예정이라면 간선으로 이어줌
# 그래프는 문제에 없는것을 만들어냄
# a가 최종적으로 바뀌는 과정을 그래프로 나타낼수잇음
# 간선을 타고 이동하다가 최종적으로 더이상갈곳없는 도착점으로 귀결
# 또 순환그래프라면 첫정점을 출력해준다
# 가장 어려운부분중하나 => 그래프를 창조
# 무한루프는 어떻게 할지
# 시간은 어덯게 할지
# 간선을 전부타고다니면 문제가 생긴다
# 총 10만개의 변수 - 일렬로 그래프가 타고간다면
# a가 10만번 b가 10만번-1 c가 10만번-2번 => 10만^2 => 시간초과
# 개선할 방법 모르겠다면 그냥 내라
# 그런데 빠르게하는 방법으 찾는다면...?
# 딕셔너리 자료구조 사용해서 찾는다
# 모든 정점에서 나가는 정점은 outedge라고 하는데
# 0개 이거나 1개이다
# 변수로 바뀌던가(1개) 단어로 바뀌던가 (0개)
# 나가는 간선이 0개인 친구들을 별표를 쳐놓는다
# 간선을 뒤집는다
# 그리고 b와 h는 c와 같다!!라고 알려주고 또 b에 이어서 a도 c와 똑같애!
# a -> b -> c 로 바뀐요량이라면 a <- b <- c 로 바꾼다면 간선의 방향이
# 어차피 a와 b는 c로 바뀌므로 c와 같아! 라고 외칠수잇다
# 거꾸로 뒤집는 생각이 많이 활용된다.....

# {a} {b} {c} {d} {e} {f} {g} {h}
# 8
# a {b}
# b {c}
# h {c}
# g {d}
# d {e}
# e {f}
# f {d}
# c itisC

import sys
from collections import defaultdict
sys.setrecursionlimit(100005) # 재귀시간 제한 => 무한루프돌수있기때문이다 10만개까지 탐색하고 다시 자신으로 돌아 올 수 있기때문에
si = sys.stdin.readline
template_string = si().strip() # 문자를 바꾼 템플릿 문자배열
n = int(si())
rules = dict()   #  O(1)로 찾기 가능 => 자료구조 선택 능력
variables = set() # O(1)로 찾기 가능 => 자료구조 선택 능력
for _ in range(n):
    key, value = si().split()
    rules[key] = value  # key라는 변수가 value라는 걸로 바뀜!
    variables.add(key)
def is_variable(value): # 핵심이다 => 변수관계에 등록되어 있지도 않고 변수표현 {} 이아니라면 그냥 문자 종착점이다!!
    return value[0] == '{' and value[-1] == '}' and value[1: -1] in variables  # O(1) 만약 리스트라면 O(N)이 될것이다
outedge = defaultdict(list)
init_vars = []
for key, value in rules.items():
    # key -> value 로 바뀌는데
    if is_variable(value):  # value가 변수라면, value -> key 간선 만들어주기 => 간선을 뒤집어준다 => 왜? 어차피 c로 변환될것들이기 때문이다!!
        outedge[value[1: -1]].append(key) # 정점이 문자열이기에 dic자료구조를 사용했다 !!!
    else:  # value가 단어라면, key는 시작점 중 하나
        init_vars.append(key)  # indegree 가 0 인 정점
        # 종착점이 없다면 무한루프에 빠진다
def dfs(cur: str, changed: str) -> None: # 그래프 탐색하면서 시작점의 value값으로 전부 같다고 외쳐준다!!!!!
    rules[cur] = changed
    for nxt in outedge[cur]:
        dfs(nxt, changed)
for var in init_vars:
    dfs(var, rules[var])
for word in template_string.split():
    if is_variable(word):
        converted = rules[word[1: -1]] # 이제 같은문자로 다 변환된 것이 셋팅되있을 것이다
        if is_variable(converted):  # 무한 루프에 빠져버린 친구
            print(word, end=' ')
        else: # 변수관계가 아예 등록되어 있지 않은 경우는 그냥 그 변환된 변수가 종착점이다
            print(converted, end=' ')
    else: # 변수가 아니라면 문자 그자체를 출력한다 (종착점)
        print(word, end=' ')