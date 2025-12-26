# 프로그래머스 베스트앨범 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 09:41-09:54-10:08(개선)

"""
장르별로 가장 많이 재생된 노래를 2개씩 모아서 베스트 앨범 선택.
노래는 '고유번호'가 있음.
1. 속한노래가 가장많이 재생된 장르를 먼저 수록.
2. 장르 내에서 많이 재생된 노래를 먼저 수록.
3. 장르 내에서 재생횟수가 같은 노래는 고유번호가 낮은 노래를 먼저 수록.
고유 번호는 genres 의 i번으로 취급.
plays[i]는 고유번호 i의 노래의 재생횟수.
"""

from typing import List
from collections import defaultdict

def solution(genres:List[str], plays:List[int]):
    answer = []
    
    # 입력 장르를 번호순서대로 정리
    genres_dict = defaultdict(list)
    total_plays = defaultdict(int) # 장르별 총 재생 횟수를 저장할 해시
    
    for i in range(len(genres)):
        genres_dict[genres[i]].append((plays[i], i))
        total_plays[genres[i]] += plays[i] # 간단하게 합계를 누적!
        # genres_dict[genres[i]]["total_play"] += plays[i] if "total_play" in genres_dict[genres[i]] else plays[i]
        
    for k in genres_dict:
        genres_dict[k]
        
    
    # 장르별 노래 순서 재정렬.  
    for k in genres_dict:
        genres_dict[k] = sorted(genres_dict[k], key=lambda x:(-x[0], x[1])) # 플레이는 내림차순, 고유번호는 오름 차순으로 정렬해야함.
        
    # 장르별 플레이 수에 따른 재정렬(내림차순)
    total_plays = sorted(total_plays, key=lambda x:total_plays[x], reverse=True)
                
    
    # 장르별 플레이 수 기준으로 돌면서 재정렬된 
    for genre in total_plays:        
        for song in genres_dict[genre][:2]:
            answer.append(song[1])        
    
    return answer