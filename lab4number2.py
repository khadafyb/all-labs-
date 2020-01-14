def num_2():
    n=int(input("enter an n value: "))
    if n==0:
        y=1
    elif n<0:
        y=0
    else:
        y = 0
        for i in range(1,n):
            y += (1+i)/(1+i**2)
    return y
num_2()
