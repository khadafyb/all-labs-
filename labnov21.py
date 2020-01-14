def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

class Rational:
    def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b,a%b)

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.gcdenom=gcd(x,y)
        self.num=x/gcd(x,y)
        self.denom=y/gcd(x,y)
    def __str__(self):
        return str(self.num)+"/"+str(self.num)

    def __add__(self,other):
        self.sumnum=self.num+other.num
        self.sumden=gcd(self.denom,other.denom)
        numb=gcd(self.sumnum,self.sumden)
        res_n=self.sumnum/numb
        res_d=self.sumden/numb
        if res_n==0:
            print('numerator is 0')
        else: 
            print(res_n,'/',res_d)
        

    def __sub__(self,other):
        self.sumnum=self.num-other.num
        self.sumden=gcd(self.denom,other.denom)
        numb=gcd(self.sumnum,self.sumden)
        resn=self.sumnum/numb
        resd=self.sumden/numb
        if resn==0:
            print('numerator is 0')
        else: 
            print(res_n,'/',res_d)

    def __mul__(self,other):
        self.sumnum=self.num*other.num
        self.sumden=self.denom*other.denom
        numb=gcd(self.sumnum,self.sumden)
        resn=self.sumnum/numb
        resd=self.sumden/numb
        print(resn,'/',resd)

    def __truediv__(self,other):
        self.sumnum=self.num*other.denom
        self.sumden=self.denom*other.num
        numb=gcd(self.sumnum,self.sumden)
        resn=self.sumnum/numb
        resd=self.sumden/numb
        print(resn,'/',resd)
    def __float__(self):
        return self.num/self.denom

    def __eq__(self,other):
        num1=float(self)
        num2=float(other)
        if num1==num2:
            return self,'=',other
        else:
            print('not equal')
    
    def __lt__(self,other):
        num1=funny(self)
        num2=funny(other)
        if num1>num2:
            return self,'>',other
        else:
            return self,'<',other
    def __ge__(self,other):
        num1=funny(self)
        num2=funny(other)
        if num1>=num2:
            return self,'>=',other
        else:
            return self,'<=',other
        

    
