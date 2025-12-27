# 프로그래머스 도둑질 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42897
# 11:57-

"""
도둑이 마을을 털 계획을 한다.
모든 집들은 동그랗게 배치되어있다. -> 첫집과 마지막 집은 연결 되어있다.
각 집은 서로 인접한 집과 방범장치가 연결되어있고, 두 집을 털면 경보가 울린다.
각 집의 돈이 담긴 배열을 money로 주어지며, 도둑이 훔칠수있는 돈의 최대값을 리턴한다.
한번 집을 털었을때, 인접한 집의 좌표 i-1, i+1은 털면 안된다.
트리 모형과 비슷하게 접근해야하는데, 인근 좌표로는 연결되어선 안된다.
현재 좌표를 기준으로 이동 가능한 모든 좌표를 탐색한다.
이동 가능한 좌표의 돈의 합계를 더해서 최대값 max를 비교한다.
이미 이동한 좌표는 다시 이동할 필요가 없다.
직선 구조의 DP 문제 2개로 쪼갠다. -> i번 집을 터는경우|i번집을 털지 않는 경우.
"""
from typing import List

def solution(money:List):
    answer = 0
    house_num = len(money)
    
    dp = [[0]* house_num for _ in range(2)] # dp[0][i] 첫번째 집을 털 때의 합계 | dp[1][i] 첫번째 집을 안털었을때 합계
    
    for i in range(house_num):        
    
        if i == 0:
            dp[0][i] = money[i]
            dp[1][i] = 0
        elif i == 1:
            dp[0][i] = dp[0][i-1]
            dp[1][i] = money[i]
            
        elif i < house_num -1:
            dp[0][i] = max(dp[0][i-1], dp[0][i-2] + money[i])
            dp[1][i] = max(dp[1][i-1], dp[1][i-2] + money[i])
        else:
            dp[0][i] = dp[0][i-1]
            dp[1][i] = max(dp[1][i-1], dp[1][i-2] + money[i])
                
    answer = max(dp[0][house_num-1], dp[1][house_num-1])
    
    return answer

if __name__ == "__main__":
    print(solution([1, 2, 3, 1]))