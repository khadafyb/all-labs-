m=int(input("enter number of columns: "))
n=int(input("enter number of rows: "))
for i in range(n):
    for j in range(m):
        print (j*(("+-")*j+"+"))
        print(j*(("| ")*j+("|"))
