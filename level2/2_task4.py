class Fibonacci:
    def __init__(self,term):
        self.term=term
    
    def generate(self):
        a=0
        b=1
        for i in range (self.term):
            print(a,end=" ")
            a,b=b,a+b

n=int(input("Enter number of terms: "))
f=Fibonacci(n)
f.generate()