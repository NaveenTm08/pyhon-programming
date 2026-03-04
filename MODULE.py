class Calc():
    def add(self,a=1,*ag):
        for i in ag:
            a+=i
        print(a)


    def sub(self,b=1,*ag):
        for i in ag:
            b -=i
        print(b)

    def mul(self,c=1,*ag):
        for i in ag:
            c*=i
        print(c)
    def dev(self,d=1,*ag):
        for i in ag:
            d/=i
        print(d)
    
n = Calc()
n.dev(10,5)

