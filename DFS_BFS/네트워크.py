# 프로그래머스 네트워크 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

"""
네트워크로 묶여있는 컴퓨터들의 총 네트워크 개수를 구해야함.
컴퓨터와 컴퓨터를 연결하는 것을 '네트워크'라고하고 연결 정보를 2차원배열로 제공함.
컴퓨터 개수 n 과 컴퓨터간의 네트워크 연결상태 computers 2차 리스트가 제공. 자기자신은 네크워크가 항상 1.
연결된 모든 컴퓨터들은 '하나의' 네트워크로 구성. 즉 연결이 안된 컴퓨터들의 묶음이 몇개인지 찾아야함.
모든 리스트들을 확인해야하므로 DFS를 사용.
"""
from typing import List
import sys
sys.setrecursionlimit(10**6)


def solution(n:int, computers:List[List[int]]):
    # 모든 컴퓨터를 확인해야하며, 이미 방문한 컴퓨터를 체크할 visited 리스트를 사용.
    visited = [False] * n # 컴퓨터는 n개
    network_num = 0
    
    # 방문하지 않은 컴퓨터 발견 시 새로운 네트워크를 시작. 카운트를 올리고 dfs를 시작한다.
    for i in range(n):
        if visited[i] == False: # 방문하지 않은 컴퓨터라면 dfs를 사용하여 연결된 네트워크를 확인. visited 리스트는 dfs와 공유.
            dfs(computers, i, visited)
            network_num += 1 # 지정된 컴퓨터와 연결된 모든 컴퓨터(노드)를 확인하였으면 네트워크 수를 하나 늘린다.

    return network_num

def dfs(computers:List[List[int]], v:int, visited:List[bool]):
    # 현재 컴퓨터 v 를 기준으로 방문 가능한 컴퓨터들을 확인한다.
    visited[v] = True
    
    for i in range(len(computers)):
        if computers[v][i] == 1 and visited[i] == False:
            dfs(computers, i, visited)
            
def solution2(n:int, computers:List[List[int]]):
    com_dict = {}
    for c in range(n):
        com_dict[c] = [i for i in range(n) if computers[c][i] == 1]
                
    visited = [False] * n # 컴퓨터는 n개
    network_num = 0
    
    for i in range(n):
        if visited[i] == False:
            dfs2(com_dict, i, visited)
            network_num += 1
            
    return network_num
                
def dfs2(com_dict:dict, v:int, visited:List[bool]):
    # 현재 컴퓨터 v 를 기준으로 방문 가능한 컴퓨터들을 확인한다.
    visited[v] = True
    
    for neighbor in com_dict[v]:
        if visited[neighbor] == False:
            dfs2(com_dict, neighbor, visited)
    