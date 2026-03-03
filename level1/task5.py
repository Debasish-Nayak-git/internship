class PalindromeChecker:
    def __init__(self,text:str):
        self.text=text
    def is_Palindrome(self) ->bool:
        cleaned=''.join(char.lower() for char in self.text if char.isalnum())
        return cleaned == cleaned[::-1]

if __name__=="__main__":
    user_input=input("Enter a string: ")
    checker=PalindromeChecker(user_input)

    if checker.is_Palindrome():
        print("It is a Palindrome.")
    else:
        print("It is not a Palindrome. ")
