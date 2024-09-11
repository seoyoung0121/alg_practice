from collections import deque 
N, M = map(int, input().split())
maze=[]
for i in range(N):
    maze.append(list(map(int, input())))

visited=[[0]*M for _ in range(N)]
x=0
y=0
four_dir=[(0,1),(0,-1),(1,0),(-1,0)]

queue=deque()
queue.append((0,0))
while queue:
    x, y=queue.popleft()
    for fx, fy in four_dir:
        nx=x+fx 
        ny=y+fy
        if 0<=nx<N and 0<=ny<M and maze[nx][ny]==1:
            queue.append((nx,ny))
            maze[nx][ny]=maze[x][y]+1
            
print(maze[N-1][M-1])                  
                    