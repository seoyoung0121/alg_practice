import copy

def dfs(numbers, calc):
    if len(numbers)==1:
        return numbers[0], numbers[0]
    result=[]
    for i in range(4):
        if calc[i]:
            new_calc=copy.deepcopy(calc)
            new_calc[i]-=1
            min_num, max_num=dfs(numbers[:-1], new_calc)
            if i==0:
                result.append(min_num+numbers[-1])
                result.append(max_num+numbers[-1])
            elif i==1:
                result.append(min_num-numbers[-1])
                result.append(max_num-numbers[-1])
            elif i==2:
                result.append(min_num*numbers[-1])
                result.append(max_num*numbers[-1])
            else:
                if min_num<0:
                    result.append(-((-min_num)//numbers[-1]))
                else:
                    result.append(min_num//numbers[-1])
                if max_num<0:
                    result.append(-((-max_num)//numbers[-1]))
                else:
                    result.append(max_num//numbers[-1])
                
    return min(result), max(result)
    
    
    

N=map(int, input())
numbers=list(map(int, input().split()))
calc= list(map(int, input().split()))

min_num, max_num=dfs(numbers, calc)
print(max_num)
print(min_num)



