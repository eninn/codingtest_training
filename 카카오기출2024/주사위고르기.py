# 카카오 기출 주사위고르기 문제.
# https://school.programmers.co.kr/learn/courses/30/lessons/258709
# 17:45-18:30, 19:10-19:29

"""
Docstring for 카카오기출2024.주사위고르기
a, b, 둘이 있고 n개 주사위를 사용한다.
6면에 각각 1~n의 번호를 가지고, 주사위에 쓰인 구성은 모두 다르다.
a가 n/2를 가져가면 b가 나머지 n/2를 가져간다.(항상 짝수 세트로 제공.)
각각 가져간 주사위를 모두 굴린다음 나온 수들의 합을 모두 합해 점수를 계산하고 더 큰쪽이 승리, 같으면 무승부.
주사위에 쓰인 수의 구성을 담은 2차원 정수 배열 dice가 주어짐.
A가 승리할 확률이 가장 높아지기 위해 골라야하는 주사위 번호를 오름차순으로 1차원 정수배열에 담아서 리턴해야함.
이 문제는 모든 경우를 다 세어서 승패를 비교해야하는가?
이분 탐색-투포인터 와 딕셔너리를 사용한 합계 빈도수 기록을 활용하자.
"""
from typing import List
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(dice:List[List[int]]):
    answer = []

    n = len(dice)
    
    indices = range(n)
    all_indices = set(indices)
    
    best_combination = []
    max_wins = -1
    
    for a_indices in combinations(indices, n//2):
        a_set = set(a_indices)
        b_indices = tuple(all_indices - a_set)
    
        a_sum_dict = get_sum_dict(a_indices, dice)
        b_sum_dict = get_sum_dict(b_indices, dice)
        
        a_sorted_keys = sorted(a_sum_dict.keys())
        b_sorted_keys = sorted(b_sum_dict.keys())
        
        # b의 등장 가능한 점수를 오름차순으로 정렬한 후, (key, 누적등장횟수) 형태의 튜플리스트로 재작업한다.
        current_sum = 0
        cumulative_b_counts = []
        for key in b_sorted_keys:
            current_sum += b_sum_dict[key]
            cumulative_b_counts.append((key, current_sum))
            
        total_wins = 0
        for a in a_sum_dict:
            idx = bisect_left(b_sorted_keys, a)
            
            if idx > 0:
                total_wins += a_sum_dict[a] * cumulative_b_counts[idx-1][1]
            elif idx == 0:
                continue

        if max_wins < total_wins:
            max_wins = total_wins
            best_combination = a_indices
            
    answer = [x+1 for x in best_combination]

    return answer

def get_sum_dict(selected_indices, dice):
    current_sums = {0: 1}
    
    for idx in selected_indices:
        next_sums = defaultdict(int)
        for s in current_sums:
            for face in dice[idx]:
                next_sums[s+face] += current_sums[s]
        current_sums = next_sums
    
    return current_sums

if __name__ == "__main__":
    print(solution([[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]))