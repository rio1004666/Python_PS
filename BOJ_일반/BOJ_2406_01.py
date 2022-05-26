import sys
input = sys.stdin.readline
#sys.stdin=open("input.txt", "rt")

# 부모의 값을 찾는 함수
def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

# 부모의 값을 합치는 함수
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
# 1. parent배열의 기본 값을 세팅해준다.
parent=list(range(n+1))

# 2. 연결된 지사컴퓨터의 입력을 받는다.
for _ in range(m):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

input() #첫번째 입력은 날린다 (1번 컴퓨터는 연결이 되어 있지 않아도 되므로...)
# 3. 아직 아무 것도 연결이 되지 않은 값을 구한다.
edges = []
for i in range(1,n):
    ins = list(map(int,input().split()))
    for j in range(i+1,n):
        edges.append((ins[j],i+1,j+1))
edges.sort()

# 4. 소팅한 낮은 값을 기준으로 크루스칼 알고리즘을 수행한다.
x = 0
k = 0
res=[]
for edge in edges:
    if find_parent(parent,edge[1]) != find_parent(parent,edge[2]):
        union_parent(parent,edge[1],edge[2])
        res.append((edge[2],edge[1]))
        x += edge[0]
        k += 1
print(x,k)
for r in res:
    print(r[0],r[1])