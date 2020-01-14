def num_finder(n):
    numlist=[]
    for i in range(0,n):
          if (i**2) % 4==1 and (i**3) % 5==4 and (i**4)% 6 ==3:
              numlist.append(i)
    return numlist
