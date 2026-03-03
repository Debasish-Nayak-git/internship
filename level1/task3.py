import re
class EmailValidator:
    def __init__(self,email:str):
        self.email=email.strip()
    def is_valid_format(self) ->bool:
        pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.fullmatch(pattern, self.email))
    def validate(self) ->str:
        if not self.email:
            return "Invalid : Email cannot be empty"
        if "@" not in self.email:
            return "Invalid: missing '@' symbol"
        if self.is_valid_format():
            return "Valid Email Address"
        return "Invalid Email Format"
if __name__=="__main__":
    user_email=input("Enter email address:")
    validator=EmailValidator(user_email)
    result=validator.validate()
    print(result)