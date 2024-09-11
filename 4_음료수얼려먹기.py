N, M=map(int, input().split())

array=[]
for i in range(N):
    array.append(list(map(int, input())))

visited=[[0]*M for _ in range(N)]


def DFS(i,j):
    nearby=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for x,y in nearby:
        if 0<=x<N and 0<=y<M and array[x][y]==0 and visited[x][y]==0: 
            visited[x][y]=1
            DFS(x,y)
    
answer=0
for i in range(N):
    for j in range(M):
        if array[i][j]==0 and visited[i][j]==0:
            DFS(i,j)
            answer+=1
            
print(answer)
