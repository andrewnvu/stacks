#using the created stack.py file find a way to reverse a string incorporating the file
from stack import *

def reverseString(string):
    s = Stack()
    rev_string = ""
    for _ in range (len(string)):
        s.push(string[_])
    
    while not s.is_empty():
        rev_string += s.pop()

    return rev_string


print(reverseString("abcde"))