from functools import cmp_to_key

def solution(numbers:list):
    # 모든케이스를 다만들면 너무 오래걸림
    # 정렬 방식을 변경하여 두 수의 제일 왼쪽의 수가 앞으로 오도록 재정렬해야함. 
    
    numbers = [str(n) for n in numbers]
    numbers.sort(key=cmp_to_key(compare))
    answer = "".join(numbers)
    
    return "0" if answer[0] == "0" else answer
        
def compare(a:str, b:str):
    # a값과 b 값의 우선순위를 결정할때 오름차순기준: a<b: -1, a>b: 1, 0은 순서상관없음.
    # 두 문자열을 붙였을때 큰 순서를 판별
    # 파이썬에서 str 끼리 대소 비교는 유니코드 값을 비교하므로 9>10 이 된다.
    if a + b > b + a:
        return -1
    else:
        return 1
    
        
print(solution([3, 30, 34, 5, 9]))