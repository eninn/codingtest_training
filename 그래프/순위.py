"""
권투선수 n명 1~n번까지.
A선수가 B선수보다 실력이 좋다면 항상 A가 B를 이김.
정확하게 순위를 매길 수 있는 선수의 수를 리턴해야함.
각 노드에대해서 (승리횟수, 패배횟수) 가 기록되어야함. 각 승리횟수 패배횟수는 부모노드에서 상속받아서 누적시킴.
승리+패배=n-1 이라면 해당 선수는 정확한 등수를 매길 수 있음.
플로이드-워셜 알고리즘: 3중for문을 사용. 거쳐가는노드K, 출발노드I, 도착노드J를 돌면서 
"""

def solution(n:int, results:list):
    answer = 0
    matrix= [[0]*n for _ in range(n)] # win/lose 표기 표.
    
    for result in results:
        matrix[result[0]-1][result[1]-1] = 1
    
    for k in range(n): # 확인노드
        for i in range(n): # 출발
            for j in range(n): # 도착
                if matrix[i][k] == 1 and matrix[k][j] == 1: # i가 k를 이겼고, k가 j를 이겼다면
                    matrix[i][j] = 1 # i는 자동으로 j를 이겼음.
                
    for i in range(n):
        count = 0
        for j in range(n):
            if matrix[i][j] == 1 or matrix[j][i]: # i에 대해서 j를 이겼거나 또는 j한테 졌을경우 간선 추가.
                count += 1
        if count == n - 1: # 해당 노드가 모든 노드와 간선으로 연결되어있다면 등수를 확정가능.
            answer += 1 
    
    return answer


    
print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))