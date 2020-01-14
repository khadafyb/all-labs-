def fibonacci(n):
    fiblist=[0,1]
    for i in range(n-2):
        q=fiblist[-1]+fiblist[-2]
        fiblist.append(q)
    return fiblist
        
