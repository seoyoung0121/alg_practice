N, M=map(int, input().split())
answer=0
for i in range(N):
    numbers=list(map(int, input().split()))
    min_num=min(numbers)
    if min_num>answer:
        answer=min_num

print(answer)