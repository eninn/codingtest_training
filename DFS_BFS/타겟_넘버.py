# 프로그래머스 타겟 넘버 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/43165

"""
numbers 는 n개의 정수 리스트로 구성됨.
리스트를 끝까지 찾아가면서 +,-를 반복해서 사용하고, 끝까지 도착했을 때 target 숫자가 되면 카운트를 늘린다.
dfs 재귀함수를 구성하는데, 전체 그래프 정도와 현재 값을 받고 
최종 리턴은 카운트된 숫자를 반환.
"""

import sys
sys.setrecursionlimit(10**6)
target_matched = []

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    
    return sum(target_matched)
    
def dfs(numbers:list, target:int, pos:int, v_sum:int):
    if pos == len(numbers):
        if v_sum == target:
            target_matched.append(1)
    else:   
        dfs(numbers, target, pos+1, v_sum+numbers[pos])
        dfs(numbers, target, pos+1, v_sum-numbers[pos])