# 프로그래머스 N으로표현 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 15:38-16:22

"""
숫자 N과 사칙연산을 사용해서 숫자 num 표현하기.
N의 사용횟수중 최소값을 리턴한다.
괄호와 사칙연산을 사용할 수 있고 나누기 연산에서 나머지는 무시한다.
최소값이 8보다 클 경우 -1을 리턴하여 종료.
숫자 N이 몇개 사용되었는지를 봐야함.
N은 1~9사이의 수
동적계획법(DP)는 작은 문제의 답을 결합하여 큰 문제를 해결하는 방법에 있음.
"""

import sys
sys.setrecursionlimit(10**6)

def solution(N:int, number:int):
    # N을 k번 썻을 때 각 사용횟수마다의 집합을 확인
    
    calc_result = [set() for _ in range(8)]
    
    # 먼저 N, NN, NNN 과 같이 이어사용하는 경우의수
        
    for i, calc in enumerate(calc_result):
        calc.add(int(str(N)*(i+1)))
        
    if number in calc_result[0]:
        return 1
        
    # i는 N을 사용한 횟수 1부터 시작하는 이유는 연산 N 이 0인 경우는 필요없으므로.
    for i in range(1, 8):
        for j in range(i):
            for a in calc_result[j]:
                for b in calc_result[i-j-1]:
                    calc_result[i].add(a+b)
                    calc_result[i].add(a-b)
                    calc_result[i].add(a*b)
                    if b != 0:
                        calc_result[i].add(a//b)
                    
        if number in calc_result[i]:
            return i+1
    
    return -1

    
    
if __name__ == "__main__":
    print(solution(5, 12))