def solution(strings):
    strings.sort()
    
    for i in range(len(strings) - 1):
        if strings[i + 1].startswith(strings[i]):
            return False
    
    return True