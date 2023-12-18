
def is_balanced(expression):
    stacks = []
    bracket = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '({[':
            stacks.append(char)
        elif char in ')}]':
            if not stacks or stacks[-1] != bracket[char]:
                return False
            stacks.pop()

    return not stacks

print(is_balanced("([]{()})")) 
print(is_balanced("([{)})"))   
print(is_balanced("(){}["))    

print('_'*60)