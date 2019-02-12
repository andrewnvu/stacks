#check to see if parenthesis string is a balanced string using stacks
#ex. {}{}{}{}   returns True
#ex. []]        returns False
#ex [{([()])}]  returns True

from stack import Stack

def is_match(p1, p2):
    if p1 + p2 in ['[]','()','{}']:
        return True
    else:
        return False


def balanced(myParenString):
    s = Stack()
    is_balanced = True
    index  = 0

    while index < (len(myParenString)) and is_balanced:
        if myParenString[index] in "([{":
            s.push(myParenString[index])
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, myParenString[index]):
                    is_balanced = False
        index += 1

    if is_balanced and s.is_empty():
        return True
    else:
        return False

print(balanced("[]{[]"))