class Calculater:
    def __init__ (self,num1:float,num2:float,operator:str):
        self.num1=num1
        self.num2=num2
        self.operator=operator
    def calculate(self):
        if self.operator=="+":
            return self.num1+self.num2
        elif self.operator=="-":
            return self.num1-self.num2
        elif self.operator=="*":
            return self.num1*self.num2
        elif self.operator=="/":
            if self.num2==0:
                return "Error : Division by zero"
            return self.num1/self.num2
        elif self.operator=="%":
            if self.num2==0:
                return "Error : Modulo by zero"
            return self.num1 % self.num2
        else:
            return "Invalid Operator"
if __name__=="__main__":
    try:
        number1=float(input("Enter first number"))
        number2=float(input("Enter second number"))
        op=input("Enter operator (+,-,*,/,%):")
        
        obj=Calculater(number1,number2,op)
        result=obj.calculate()
        print("Result: ",result)
    except:
        print("Invalid input.Please enter numeric values.")
        