class Power:
    def __init__(self,n,p):
        self.n=n
        self.p=p

    def pow(self):
        print(self.n**self.p)

a=int(input("Enter the number: "))
b=int(input("Enter the power: "))
result=Power(a,b)
result.pow()