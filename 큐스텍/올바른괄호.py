def solution(s):
    stack = []
    
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            try:
                stack.pop()
            except IndexError:
                return False
            
    if stack:
        return False
    
    return True