def solution(arr):
    stack = []
    temp = None
    
    for a in arr:
        if a != temp:
            stack.append(a)
        temp = a
        
    return stack