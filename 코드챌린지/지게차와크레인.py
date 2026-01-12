"""
Docstring for 코드챌린지.지게차와크레인
n,m 크기의 맵에 컨테이너가 위치한다. 특정 종류 컨테이너 출고요청이 오면 접근 가능한 해당종류의 컨테이너를 모두 꺼낸다.
일반 지게차(한번요청)는 외부에서 접근가능한 컨테이너를 뺄 수 있다.
크레인(두번요청)은 맵 내의 모든 컨테이너를 꺼낼 수 있다.
모든 요청이 완료된다음 남은 컨테이너의 수를 리턴하도록 함수를 설계해라.
작업 요청마다 처리를 해도 될거같은데.
"""
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0] # 상하좌우

def solution(storage, requests):
    answer = 0
    
    n = len(storage) # 세로
    m = len(storage[0]) # 가로
    answer = n*m
    
    containers = [[False]*(m+2) for _ in range(n+2)]
    for i, s in enumerate(storage):
        for j, container in enumerate(s):
            containers[i+1][j+1] = container
                
    
    def get_passages():
        passages = [(0,0)]
        queue = deque([(0,0)])
        passage_visited = [[False]*(m+2) for _ in range(n+2)]
        while queue:
            current_pos = queue.popleft()
            passages.append(current_pos)
            for d in range(4):
                next_pos = (current_pos[0]+dy[d], current_pos[1]+dx[d])
                if next_pos[0] < 0 or next_pos[0] >= n+2 or next_pos[1] < 0 or next_pos[1] >= m+2:
                    continue 
                if not containers[next_pos[0]][next_pos[1]] and not passage_visited[next_pos[0]][next_pos[1]]:
                    queue.append(next_pos)
                    passage_visited[next_pos[0]][next_pos[1]] = True
        return passages
    
    def liftcar(target, passages):
        nonlocal answer
        for passage in passages:
            for d in range(4):
                i, j = passage[0]+dy[d], passage[1]+dx[d]
                if i < 0 or i >= n+2 or j < 0 or j >=m+2:
                    continue
                if containers[i][j] == target:
                    containers[i][j] = False
                    answer -= 1
                        
    def crane(target):
        nonlocal answer
        for i in range(1, n+2):
            for j in range(1, m+2):
                if containers[i][j] == target:
                    containers[i][j] = False        
                    answer -= 1
                    
                    
    for request in requests:
        if len(request) == 1:
            passages = get_passages()
            liftcar(request, passages)
        elif len(request) == 2:
            crane(request[0])


    return answer



print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"] 	,["A", "BB", "A"] ))