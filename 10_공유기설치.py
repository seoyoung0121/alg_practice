def binary_search(start, end, left, visited):
    
    if left>2: #다시 이진탐색 가야함
        mid_value=(house[start]+house[end])//2
        
        mid_idx=0
        if mid_value not in house: 
            nearest_idx=start
            gap=mid_value-house[start]
            for i in range(start, end):
                n_gap=abs(mid_value-house[i]) #절댓값
                if n_gap<gap:
                    gap=n_gap
                    nearest_idx=i
        
            mid_value=house[nearest_idx]  
            mid_idx=nearest_idx
        else: 
            mid_idx=index(house, mid_value) ###인덱스 찾기
        visited.append(mid_value)
        left-=1
        binary_search(start, mid_idx-1, left, visited)
        binary_search(mid_idx+1, end, left, visited)
        
    if left==1:
        binary_search(start, mid_idx-1)
        binary_search(mid_idx+1, end)
    
    
    
              

        
    
    
    
    
    

N, C=map(int, input().split())
global house=[]
for i in range(N):
    house.append(map(int, input()))
    
house.sort()
visited=[house[0],house[-1]]
left=N-2

start=0
end=len(house)

binary_search(start, end, left, visited)




##완벽히 틀림! 거리를 얼마로할지 정한 다음 그에 맞춰서 계산!

    
    