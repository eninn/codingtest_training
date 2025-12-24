# 프로그래머스 게임 맵 최단거리
# https://school.programmers.co.kr/learn/courses/30/lessons/1844

"""
최대한 빠르게 -> BFS 문제. 큐에서 (노드, 거리) 튜플 형식으로 경로의 길이를 파악한다.
격자이동 시 4방 좌표를 구성하여 반복문으로 사용한다. 방문한 노드는 set이나 graph[nx][ny] = 0 으로 메모리 관리.
0을 만나면 이동불가, 1을 만나면 이동 가능하다.
(1,1)에서 시작하여 (n,m)으로 이동해야함.
데이터는 갈수있는길 1과 갈수없는길 0 으로 구성된 2차 리스트로 제공됨."""

from collections import deque
from typing import List
# 상, 하, 좌, 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def solution(maps:List[List[int]]):
    answer = -1    
    answer = bfs(maps, (0,0,1)) # (y, x, distence) 순서로 기록
    
    return answer

def bfs(graph:List[List[int]], start:set):
    queue = deque([start])
    graph[start[0]][start[1]] = 0
    
    n = len(graph) # 상하
    m = len(graph[0]) # 좌우
    
    if graph[n-1+dy[0]][m-1+dx[0]] == 0 and graph[n-1+dy[2]][m-1+dx[2]] == 0:
        return -1
    
    while queue:
        # 큐에서 노드를 꺼내고 사방의 이동 가능성을 확인
        current_node = queue.popleft()
        
        if current_node[0] == n-1 and current_node[1] == m-1:
            return current_node[2]
        
        for i in range(4): # top, down, left, right
            next_node = (current_node[0]+dy[i], current_node[1]+dx[i], current_node[2]+1)
            if next_node[0] >= 0 and next_node[0] < n:
                if next_node[1] >= 0 and next_node[1] < m:
                    if graph[next_node[0]][next_node[1]] == 1:
                        queue.append(next_node) # 지나간 노드 추가.
                        graph[next_node[0]][next_node[1]] = 0 # 지나간 경로는 돌아가지 않도록 설정.
                        # 이미 지나간 경로를 0 으로 설정하여 돌아가는 길은 더이상 노드가 추가되지 않도록 함.
        
    return -1
