    n=int(input("enter number of years: "))
    pay=int(input("enter original payment: "))
    interest=int(input("enter interest rate: "))
    month=n*12
def rates():
    for i in range(0,n):
        pay= pay+i*(interest*pay)
def interval_interest():
    for i in range(0,month):
        pay =pay+i*((interest/12)*pay)
    
