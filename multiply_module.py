from input_variables import a , b
from secrets import api_key
from login import user_name,pass_word

def multuply(a,b):
    if api_key:
        if user_name == "01" and pass_word =="001":
            print("API key present and loggedin")
            return a*b


    