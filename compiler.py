from math import*
def isprime(x):
    if int(x)!=x:
        return False
    if x<=1:
        return False
    elif 2<=x<=3:
        return True
    else:
        for y in range(1,floor(sqrt(x))+1):
            if not x%y:
                return False
        return True
def compilele(code):
    stack=eval('['+input("Enter the numbers to put on the stack, seperated by commas:\n")+']')
    for x in code:
        if x=='.':
            stack.append(stack.pop(0))
        elif x=='+':
            stack.append(stack[-1]+stack[-2])
        elif x=='p':
            stack.append(int(isprime(stack[-1])))
        else:
            raise SyntaxError('Only \'.+p\' is allowed')
    return stack[-1]
print(compilele(input("What code do you want to run?\n")))