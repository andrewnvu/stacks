#using stack.py convert the integer to binary
from stack import *

def convert_int_to_bin(input_integer):
    s = Stack()
    while input_integer > 0 :
        remainder = input_integer % 2 
        s.push(remainder)
        input_integer = input_integer//2
    binary =""
    while not s.is_empty():
        binary += str(s.pop())
    return binary


print(convert_int_to_bin(242))

