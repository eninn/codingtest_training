from collections import defaultdict

def solution(s):
    
    s_dict = defaultdict(int)
    
    for string in s:
        s_dict[string] += 1
        
    ordering = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
    
    
    
print(solution("abbbee"))