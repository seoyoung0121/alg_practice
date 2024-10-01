from collections import deque 
N, M, K, X=map(int, input().split())

road=[[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a, b=map(int, input().split())
    road[a][b]=1
    road[b][a]=1 #단방향 노드라서 틀림!
    
q=deque()
q.append((X,0))
visited=[0]*(N+1)
visited[X]=1
while q:
    loc, dist=q.popleft()
    for j in range(1,N+1):
        if visited[j]==0 and road[loc][j]==1:
            q.append((j,dist+1))
            road[X][j]=dist+1
            road[j][X]=dist+1
            visited[j]=1
flag=0
for i in range(N+1):
    if road[X][i]==K:
        flag=1
        print(i)
if flag==0:
    print(-1)