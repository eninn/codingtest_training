# 프로그래머스 등굣길 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 17:26-18:00+09:17-09:23

"""
격자모양 지도(m*n)에서 물에 잠긴 좌표 puddles를 회피하여, 오른쪽과 아래로만 움직여 집에서 학교까지 갈수있는 최단경로 개수를
1_000_000_007로 나눈 나머지로 리턴.
최단경로 개수를 모두 계산해야함.
맵을 만들고 각 칸을 확인하면서 해당 칸으로 올수있는 경우의 수를 기록한다.
"""
from typing import List
import sys

def solution(m:int, n:int, puddles:List):
    answer = 0
    
    # 맵을 그리고 아직 이동하지 않은곳을 0 으로 설정.
    map = [[0]*m for _ in range(n)]
    
    # 웅덩이가 생긴곳은 -1로 설정해줌.
    for puddle in puddles:
        map[puddle[1]-1][puddle[0]-1] = -1
    
    for i in range(n):
        for j in range(m):
            if map[i][j] == -1:
                continue
            
            if i == 0 and j == 0:
                map[i][j] = 1            
            elif j == 0:
                if map[i-1][j] == -1:
                    map[i][j] = 0
                else:
                    map[i][j] = map[i-1][j]
            elif i == 0:
                if map[i][j-1] == -1:
                    map[i][j] = 0
                else:
                    map[i][j] = map[i][j-1]
            else:
                if map[i-1][j] == -1:
                    map[i][j] = map[i][j-1]
                elif map[i][j-1] == -1:
                    map[i][j] = map[i-1][j]
                else:
                    map[i][j] = map[i-1][j] + map[i][j-1]
            
    answer = map[n-1][m-1]
                
    return answer % 1_000_000_007



if __name__ == "__main__":
    print(solution(4, 3, [[2, 2]]))
    