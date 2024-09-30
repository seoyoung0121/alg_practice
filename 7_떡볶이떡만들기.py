N, M=map(int, input().split())
tteok=list(map(int, input().split()))
tteok.sort()

sum=0
index=0
for i in range(len(tteok)):
    sum+=max(0,tteok[i]-tteok[-2])

if sum<M:
    for i in range(len(tteok)-3, 0, -1): 
        gap=tteok[i+1]-tteok[i]
        time=len(tteok)-i-1
        sum+=gap*time 
        if sum>=M:
            index=i
            break
    
print(tteok[index])