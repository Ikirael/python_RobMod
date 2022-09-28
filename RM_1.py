'''
необходимо проверить что открывающие и закрывающие скобки
расставленные верно.
'''
def CheckBr(text):
    open = ["<","(","{","["]
    close = [">",")","}","]"]
    stack = [] 
    for char in text:
        if char in open: 
            stack.append(open.index(char))
        elif char in close: 
            if stack and stack[-1] == close.index(char):
                stack.pop()  
            else:
                return False 
                             
    return (not stack) 

text = input()
if CheckBr(text):
    print ("True")
else:
    print("False")