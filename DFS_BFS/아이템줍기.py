# 프로그래머스 아이템 줍기 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/87694

"""
좌표 내에 겹쳐진 직사각형들로 표현된 범위에서 캐릭터가 가장 바깥 테두리를 따라 이동하는 조건을 가짐.
겹쳐진 직사각형들 속에 빈공간이 있어도 가장 바깥 테두리를 캐릭터 경로로 설정함.
서로다른 직사각형의 x,y축의 좌표가 같은 경우는 나오지 않음.
모든 직사각형은 서로 겹쳐지며, 두개로 분리된 지형도 나오지 않음.
한 직사각형 내에 다른 직사각형이 완전히 포함되지도 않음.
직사각형 배열 rectangle, 캐릭터 초기위치, 아이템 위치가 작성되며, 캐릭터가 아이템을 줍기위해 이동하는 가장 짧은거리를 구해야함.
ractangle의 배열은 [x1, y1, x2, y2]로 구성된다.(좌측하단, 우측상단)
ractangle은 최소1개부터 최대 4개까지 등장할수있다.
아이템과 캐릭터는 다각형 테두리 위의 점으로 주어진다.
짧은거리 문제이므로 BFS를 사용.
좌표 문제이므로 상하좌우를 계산하는것이 좋을듯.
주어진 ractangle 좌표를 기준으로 테두리 맵을 구하고 테두리맵을 기준으로 캐릭터가 이동하면서 가장 짧은 구간을 찾으면 될거같음.
"""
from collections import deque
from typing import List

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(rectangle:List[List[int]], characterX:int, characterY:int, itemX:int, itemY:int):
    answer = 0
    
    # 맵을 2배수 하여, 내부 공간까지 표현(인접한 경로를 뚫고 넘어가지않고 테두리를 타고갈 수 있도록 표현)
    # 최종 이동 길이를 1/2 처리.
    map = [[0]*(50*2+1) for _ in range(50*2+1)]
    
    # rectangle을 순회
    for rect in rectangle:
        for i in range(rect[0]*2, rect[2]*2+1):
            for j in range(rect[1]*2, rect[3]*2+1):
                if map[i][j] == -1:
                    continue
                if not (i == rect[0]*2 or i == rect[2]*2 or j == rect[1]*2 or j == rect[3]*2):
                    map[i][j] = -1
                else:
                    if map[i][j] == 0:
                        map[i][j] = 1 # 직사각형 테두리 표현
                        
    answer = bfs(map, (characterX*2, characterY*2, 0), (itemX*2, itemY*2))
    
    return answer // 2 

def bfs(map:List[List[int]], start:set, end:set):
    queue = deque([start])
    map[start[0]][start[1]] = 0 # 이동 시작.
    
    while queue:
        current_pos = queue.popleft()
        
        if current_pos[0] == end[0] and current_pos[1] == end[1]:
            return current_pos[2]
        
        for i in range(4):
            # 다음 경로 확인해서 이동 가능한지 확인.
            next_pos = (current_pos[0]+dx[i], current_pos[1]+dy[i], current_pos[2]+1)
            
            # 다음 경로가 맵 내부에 위치하는지 확인하는 로직이 필요함.
            if next_pos[0] < 0 or next_pos[0] >= len(map):
                continue
            if next_pos[1] < 0 or next_pos[1] >= len(map[0]):
                continue
            
            if map[next_pos[0]][next_pos[1]] == 1:
                queue.append(next_pos)
                map[next_pos[0]][next_pos[1]] = 0
                
    return -1

if __name__ == "__main__":
    
    print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))