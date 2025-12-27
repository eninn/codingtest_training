# 프로그래머스 사칙연산 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/1843
# 09:39-10:44

"""
사칙연산에서 +는 결합이 가능하고, -는 결합이 안된다.(연산순서대로 계산해야함)
숫자와 연산기호가 arr로 주어질때 서로다른 연산 순서의 계산결과의 최대값을 구한다.
각 연산들의 결과를 저장하면서 다른 조합이 들어왔을때 최종 결과를 비교해야한다.
모든 경우의 수를 확인하긴 해야함. -> 연산량 줄이기.
마이너스 연산이 있다면 덩어리의 최소를 만들 수 있음.
"""
from typing import List

def solution(arr: List[str]):
    answer = -1
    numbers = [int(x) for x in arr[::2]]
    ops = arr[1::2]
    n = len(numbers)
    
    # 연산의 최대, 최소값을 저장하는 dp 테이블.
    # 마이너스 부호가 뒤에오면 값을 최대로 만들 수 있다.
    min_dp  = [[float('inf')] * n for _ in range(n)]
    max_dp  = [[-float('inf')] * n for _ in range(n)]
    
    # 1. 자기 자신인 경우 -> 구간 길이가 [i][i] 일때 자기자신의 값은 그대로 넣는다.
    for i in range(n):
        min_dp[i][i] = max_dp[i][i] = numbers[i]
        
    # 2. 길이가 k 인 구간을 구한다. 구간이 i~j 일때, 그 사이의 연산자 k를 기준으로 반을 가른다.
    # 즉 [i~k] 구간과 [k+1~j] 로 구간이 나뉘어진다.
    for length in range(2, n+1): # 구간에 포함된 숫자의 갯수
        for i in range(n-length+1): # 구간 시작점
            j = i + length - 1 
            for k in range(i, j): # i지점과 j 지점 사이의 연산자 k 위치
                
                if ops[k] == '+':
                    # 연산자가 + 일때 -> 가장 큰 값과 가장 큰 값을 더한다. -> 최대값 | 가장 작은값과 가장 작은값을 더한다 -> 최소값.
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                elif ops[k] == '-':
                    # 연산자 - 일때. 가장큰값과 가장 작은값을 뺀다-> 최대값 | 가장 작은값에 가장 큰값을 뺀다 -> 최소값
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                    
                    
    return max_dp[0][n-1]

if __name__ == "__main__":
    print(solution(["1", "-", "3", "+", "5", "-", "8"]))

