def solution(numbers):
    import math
    import itertools
        
    def is_prime(x):
        if x <= 1:
            return False
        
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
            
        return True
    
    num_list = []
    for l in range(1, len(numbers) + 1):
        new = [int(''.join(x)) for x in itertools.permutations(numbers, l)]
        num_list.extend(new)
        
    result = 0
    for x in set(num_list):
        result += int(is_prime(x))
        
    return result