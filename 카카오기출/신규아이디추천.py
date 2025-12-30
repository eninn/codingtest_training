"""
카카오 2021 기출문제.
규칙에 맞지 않는 아이디가 입력되었을때 입력된 아이디와 '유사'하고 규칙에 맞도록 아이디를 추천한다.
아이디는 3자 이상 15자 이하.
아이디는 알파벳소문자, 숫자, -, _, . 만 사용 가능. 단, . 은 처음과 끝에는 사용할 수 없고 연속으로 사용할 수 없다.
7단계에 거쳐서 규칙을 검사하고 맞지 않을때 새로운 아이디를 추천한다.
"""

def solution(new_id:str):
    answer = ''
    
    answer = step1(new_id)
    
    return answer
    
def step1(new_id:str):
    # 1. 모든 대문자를 소문자로 치환.
    return step2(new_id.lower())
    
    
def step2(new_id:str):
    # 2. 알파벳 소문자, 숫자, 빼기, 밋줄, 마침표 제외 모든 문자를 제거한다.
    next_id = ""
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ["-", "_", "."]:
            next_id += c
    return step3(next_id)
    
def step3(new_id:str):
    # 3. . 이 2개 이상 반복되면 하나의 마침표로 치환.
    next_id = ""
    for i in range(len(new_id)):
        if i == 0:
            next_id += new_id[i]
            continue
        if new_id[i] == "." and new_id[i-1] == ".":
            continue
        next_id += new_id[i]
    return step4(next_id)
    
def step4(new_id:str):
    # 4. .가 처음이나 끝에 위치하면 제거.
    if new_id and new_id[0] == ".":
            new_id = new_id[1:]
    if new_id and new_id[-1] == ".":
        new_id = new_id[:-1]
    
    return step5(new_id)

def step5(new_id:str):
    # 5. new_id가 빈문자열이면 new_id에 a를 대입.
    if not new_id:
        new_id = "a"    
    return step6(new_id)

def step6(new_id:str):
    # 6. new_id 길이가 16자 이상일때, new_id의 첫 15개 문자를 제외한 나머지 문자를 모두 제거.
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        
    return step7(new_id)

def step7(new_id:str):
    # 7. new_id 길이가 2이하일 경우 new_id의 마지막 문자를 new_id 길이가 3이 될때까지 반복.   
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id   

if __name__ == "__main__":
    print(solution("=.="))