import re
class PasswordChecker:
    def __init__(self,password):
        self.password=password
    
    def check_strength(self):
        score=0
        if len(self.password) >=8:
            score+=1
        if re.search("[A-Z]",self.password):
            score+=1
        if re.search("[a-z]",self.password):
            score+=1
        if re.search("[0-9]",self.password):
            score+=1
        if re.search("[!@#$%^&*(),.?\":{}|<>]",self.password):
            score+=1
        if score <=2:
            print("Weak Password")
        elif score == 3 or score == 4:
            print("Medium Password")
        else:
            print("Strong Password")

p=input("Enter password: ")
checker=PasswordChecker(p)
checker.check_strength()