N, M=map(int, input().split())
x, y, direction= map(int, input().split())
array=[]
for i in range(N):
    array.append(list(map(int, input().split())))
    
d=[[0]*M for _ in range(N)]
d[x][y]=1
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def can_go(x,y):
    if 0<=x<N and 0<=y<M and not d[x][y] and not array[x][y]: #글로벌?
        return True
    else:
        return False

count=0
answer=1
while True:
    direction=(direction-1)%4
    count+=1
    newX=x+dx[direction]
    newY=y+dy[direction]
    if can_go(newX,newY):
        x=newX
        y=newY
        count=0
        answer+=1
        d[x][y]=1
    elif count==3:
        x-=dx[direction]
        y-=dy[direction]
        count=0
        if array[x][y]==1:
            break

print(answer)
    
    

        
