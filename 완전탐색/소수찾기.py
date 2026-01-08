import math
from itertools import permutations

def solution(numbers:str):
    answer = 0
    
    all_cases = []
    
    for i in range(1, len(numbers)+1):
        cases = list(permutations(numbers, i))
        all_cases.extend(cases)
        
    all_cases = set([int("".join(c)) for c in all_cases])
    
    for case in all_cases:
        if is_prime(case):
            answer += 1

    return answer


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(solution("011"))