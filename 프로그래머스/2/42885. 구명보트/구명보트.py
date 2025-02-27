def solution(people, limit):    
    result = 0
    left = 0
    right = len(people) - 1
    people.sort()
    
    while left <= right:
        weight = 0
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
            
        result += 1
    
    return result