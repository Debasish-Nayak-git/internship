class temparatureConverter:
    def __init__(self,value,unit):
        self.value=value
        self.unit=unit
    def to_farenheit(self):
        return (self.value * 9/5) + 32 
    def to_celsius(self):
        return(self.value-32) * 5/9
    def convert(self):
        if self.unit== 'C':
            result=self.to_farenheit()
            return f"{self.value}C is {result:.2f}F"
        elif self.unit == 'F':
            result=self.to_celsius()
            return f"{self.value}F is {result:.2f}C"
        else:
            return "Invalid unit ! Please use 'C' for celcius and 'F'for farenheit"
val=float(input("Enter the temparature value: "))
u=input("Enter the unit (C/F): ")
obj=temparatureConverter(val,u)
print(obj.convert())
