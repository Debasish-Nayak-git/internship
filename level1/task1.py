class string_manupulater:
    def __init__(self,text):
        self.text=text
    def reverse_string(self):
        return self.text[::-1]
input_data=input("enter any string : ")
processor=string_manupulater(input_data)
result=processor.reverse_string()
print("input data is ",input_data,",reverse is " ,result)
