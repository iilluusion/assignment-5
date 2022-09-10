class Power:
    def __init__(self,n,x):
        self.n=n
        self.x=x

    def pow(self):
        print(self.n**self.x)

a=int(input("Enter the number: "))
b=int(input("Enter the power: "))
result=Power(a,b)
result.pow()