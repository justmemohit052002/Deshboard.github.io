def min_jump(n):
    jump=0
    
    while(n>0):
        if n%2 ==0:
            n=n/2
        else:
            n=n-1
        jump=jump+1
    return jump

n=int(input())

result = min_jump(n)
print(result)