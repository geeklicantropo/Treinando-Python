'''
Use a stack to check wheter or not a string  has balanced usage of parenthesis.
The number of openings and closings of parenthesis must match
'''

'''
Ex.: (()) -> Balanced
     ()) -> Not balanced 
'''

from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(parent_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parent_string) and is_balanced:
        paren = parent_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False

        index +=1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

print(is_paren_balanced("()("))