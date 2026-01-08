def solution(inputs, pattern):
    answer = []
    
    # 입력 inputs에서 한 문자열 s 와 패턴이 주어짐.
    # 문자열 s에 소문자를 제거하고 pattern과 동일한 문자열을 만들 수 있으면 True, 불가능하면 False를 제출
    
    
    for input_string in inputs:
        result = pattern_check(input_string)
        answer.append(result)
    
    
    
    return answer

def pattern_check(string:str, pattern:str):
    string_point = 0 # 패턴과 맞는 string내의 문자열 시작-끝 좌표
    pattern_point = 0 # 패턴의 현재 시작-끝 좌표
    
    for i, s in enumerate(string):
        # 스트링의 처음부터 시작하면서 패턴의 처음과 동일한 글자가 있는지 탐색
        # 동일한 패턴이 탐색되면 포인트를 이동하면서 기록.
        if s == pattern[pattern_point]:
            pattern_point +=1
            string_point = i
            
        if pattern_point == len(pattern):
            return True
            
    return False
            
            
            
print(solution())