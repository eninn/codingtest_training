# 프로그래머스 단어변환 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/43163

"""
단어집합을 구하는 문제. 두개 단어 begin, target과 단어집합 words가 있음.
규칙을 이욯애서 begin에서 target 단어로 변환시키는 가장 짧은 변환과정을 찾는다.
규칙1. 한번에 한개 알파벳만 변환가능.
규칙2. word내의 단어로만 변환 가능.
변환이 불가능하면 0을 리턴.
가장 짧은 케이스를 찾아야하므로 BFS를 사용한다.
"""

from collections import deque

def solution(begin:str, target:str, words:list):
    answer = 0
    
    # 만들 수 없는 조건일때 바로 반환.
    if target not in words:
        return answer
    
    answer = bfs(begin, target, words)
    
    return answer
    
def bfs(begin:str, target:str, words:list):
    queue = deque([(begin, 0)]) # 현재 글자와 변환 횟수를 함께 기록.
    visited = set()
    
    while queue:
        current_word, count = queue.popleft()
        
        if current_word == target: # 타겟과 같은지 확인하면서 동일해졌을때 현재 변환 카운트를 전달한다.
            return count
        
        for word in words:
            # 단어를 비교해서 단어가 한개만 바뀌는지 확인해야함.
            if word in visited:
                continue
            
            diff_count = sum(1 for a, b in zip(current_word, word) if a != b)
            
            if diff_count == 1:
                queue.append((word, count+1))
                visited.add(word)
                
    # target 으로 변환이 실패하면 0을 반환.
    return 0
                
        