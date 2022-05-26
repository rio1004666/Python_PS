from collections import deque
uf=[-1]*251
def find(a):
    if uf[a]<0:
        return a
    uf[a]=find(uf[a])
    return uf[a]
def merge(a,b):
    if a>b:
        a,b=b,a
    a=find(a)
    b=find(b)
    if a==b:
        return False
    uf[b]=a
    return True

n,m=map(int,input().split())
visited=[[[-1]*n for i in range(n)] for i in range(m+1)]
arr=[]
q=deque()
cnt=0
for i in range(n):
    arr.append(list(input().strip()))
    for j in range(n):
        if arr[i][j]=='S' or arr[i][j]=='K':
            q.append([0,cnt,i,j])
            visited[cnt][i][j]=0
            arr[i][j]=cnt
            cnt+=1
dx=[0,0,-1,1]
dy=[-1,1,0,0]
res=0
while q:
    ans,idx,x,y=q.popleft()
    if m==0:
        break
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<nx<n and 0<ny<n and visited[idx][nx][ny]==-1:
            if arr[nx][ny]=='1': continue
            if arr[nx][ny]=='0':
                q.append([ans+1,idx,nx,ny])
                visited[idx][nx][ny]=ans+1
            else:
                if merge(idx,arr[nx][ny]):
                    m-=1
                    visited[idx][nx][ny]=ans+1
                    q.append([ans+1,idx,nx,ny])
                    res+=(ans+1)
if m==0:
    print(res)
else:
    print(-1)