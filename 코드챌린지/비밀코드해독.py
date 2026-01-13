"""
Docstring for 코드챌린지.비밀코드해독
1~n 안에서 서로다른 정수 5개가 오름차순으로 정렬된 비밀코드를 맞춰야함.
m번의 분석 시도 가능.
시도 마다 서로다른 정수 5개를 입력 시 몇개가 비밀코드에 포함되어있는지 확인 가능.
m번의 시도 후 비밀코드로 가능한 정수 조합의 개수를 확인해야함.
비밀코드가 없는 경우는 없음.
n<=30, m <= 10 이므로 최대 30개 중에서 5개를 순서상관없이 뽑는 경우의 수는 30C5로 작업량이 적다.
"""
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    posible_codes = list(combinations(range(1,n+1), 5))
    # answer_codes = set()
    
    for i in range(len(posible_codes)):
        for j in range(len(q)):
            intersection = set(q[j]) & set(posible_codes[i])
            if len(intersection) != ans[j]:
                break
        else:
            answer += 1
                
    # answer = len(answer_codes)
        
    
    
    return answer

print(solution(10, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [3, 7, 8, 9, 10], [2, 5, 7, 9, 10], [3, 4, 5, 6, 7]],[2, 3, 4, 3, 3]))