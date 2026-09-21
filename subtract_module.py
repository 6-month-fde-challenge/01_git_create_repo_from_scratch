from input_variables import a , b
from secrets import api_key

def subtract(a,b):
    if api_key:
        print("API key present")
        return a-b