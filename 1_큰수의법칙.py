N, M, K=map(int,input().split())

numbers=list(map(int,input().split()))
numbers.sort()
biggest_num=numbers[N-1]
second_num=numbers[N-2]

count=0
sum=0
for i in range(M):
    if count<K:
        sum+=biggest_num
        count+=1
    else:
       sum+=second_num
       count=0 
       
print(sum)