def binary_search(array, target):
    start=0
    end=len(array)-1
    while start<=end:
        mid=(start+end)//2
        if array[mid]>target:
            end=mid-1
        elif array[mid]<target:
            start=mid+1
        elif array[mid]==target:
            return "yes"
    return "no"

N=map(int, input())
tools=list(map(int, input().split()))
M=map(int, input())
finding=list(map(int, input().split()))
tools.sort()

for i in finding:
    result=binary_search(tools, i)
    print(result)
    
    


    
    