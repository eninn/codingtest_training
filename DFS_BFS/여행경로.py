# 프로그래머스 여행경로 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 15:33-16:13

"""
항공권이 제공되며 모두 사용하여 여행경로를 짠다. 항상 인천 ICN 에서 출발한다.
tickets의 각 행 [a, b]는 a에서 b로 가는 항공권이 있다는 의미이다.
주어진 항공권을 모두 사용해야함. -> DFS 로직을 사용한다.
가능 경로가 2개 이상일경우, 알파벳 순서가 앞서는 경로를 사용한다.
항상 모든 도시를 방문 가능하도록 제공된다.
*** 오일러 경로 *** 알고리즘 문제.
    현재 방문지에서 티겟의 중복사용을 방지하면서 (pop 사용) 갈수있는 모든 경로를 확인해야함.
    dfs에서 ticket_dict[current_city] 에 저장된 다음 방문지가 더이상 없을때까지 while문을 실행하며, 
    다음방문지가 없는 경우부터 순서대로 tour_list 에 저장되기 때문에 제일 마지막 방문지부터 순서대로 기록됨.
    ticket_dict는 저장되어있는 티겟들을 하나씩 사용하면서 (pop으로 제거됨) 모든 티켓이 사용되면 작업을 종료함.    
"""
from typing import List
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(tickets:List[List[str]]):
    answer = []
    
    ticket_dict = defaultdict(list)
    for ticket in tickets:
        ticket_dict[ticket[0]].append(ticket[1])
        
    for k in ticket_dict:
        ticket_dict[k] = sorted(ticket_dict[k], reverse=True)
    
    dfs(ticket_dict, current_city="ICN", tour_list=answer)
    
    # 역순으로 쌓았으므로 다시 정방향으로 돌려서 리턴.
    answer.reverse()

    return answer

def dfs(ticket_dict:List[List[str]], current_city:str, tour_list:List[str]):
    while ticket_dict[current_city]:
        # 알파벳 순서대로 공항을 먼저 꺼내면서 깊이탐색 진행.
        next_city = ticket_dict[current_city].pop() 
        dfs(ticket_dict, next_city, tour_list)
        
    # 더이상 갈 곳이 없을 때 추가.
    tour_list.append(current_city)
    
        
if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
    
    

    