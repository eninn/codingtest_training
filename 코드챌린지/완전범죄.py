"""
Docstring for 코드챌린지.완전범죄
a, b도둑이 물건을 훔칠때, 흔적이 남으며 흔적이 누적되면 경찰에 붙잡히므로 최소화해야한다.
각 도둑이 남기는 흔적의 개수는 1~3이다.
모든 물건을 훔쳤을때 a도둑이 남긴 흔적의 누적개수의 최소값을 리턴.
1<= info <= 40
1<= n <=120 n 이상이 되면 발각
1<= m <=120 m 이상이 되면 발각
흔적의 개수가 최대 40으로 적으므로 모든 케이스를 탐색하는것을 고려한다.
흔적을 누적할때 A의 누적 최소값을 리턴해야하므로 최대한 B가 누적하도록 해야함?
모든 누적을 했을때 B의 누적값이 넘지 않으면서 A의 누적값이 최소가 되어야함.
각 info에 대해서 a, b가 훔칠수 있는 모든 경우의수를 만들고 값의 합중에서 n, m보다 낮으면서 n이 최소가되는 겂을 구한다.
어떤 방법도 모두 훔칠 수 없다면 -1을 리턴.
dp 테이블을 만들고 dp[a흔적]=B의 최소흔적 으로 동적 계획법을 고려한다.
"""


def solution(info, n, m):
    answer = -1
    
    # 행 i: i번째 물건까지 훔쳤을때.
    # 열 j: 도둑 A가 지금까지 남긴 누적흔적.
    # dp[i][j]: i번 물건까지 훔쳤을때 A의 누적흔적 j일 경우 B가 남기는 최소 누적 흔적.
    dp = [[float('inf')]*121 for _ in range(121)]
    dp[0][0] = 0
    # dp[0][j] = inf # a 흔적이 j일때는 아직 모름
    
    for idx in range(1, len(info)+1):
        a_trace, b_trace = info[idx-1]
        for j in range(n): # a의 누적이 n 미만이어야함.
            if dp[idx-1][j] == float('inf'): # 누적되지 않았던 경우에는 생략
                continue
                
            # a가 훔치는 경우: A의 흔적 j가 j+a_trace 만큼 증가
            if j + a_trace < n:
                dp[idx][j+a_trace] = min(dp[idx][j+a_trace], dp[idx-1][j]) # 최소값을 유지하면서 누적
            
            # b가 훔치는 경우
            new_b_trace = dp[idx-1][j] + b_trace
            if new_b_trace < m:
                dp[idx][j] = min(dp[idx][j], new_b_trace)
                
    for last in range(len(dp[len(info)])):
        if dp[len(info)][last] != float('inf'):
            answer = last
            break
    
    return answer
    

print(solution([[1, 2], [2, 3], [2, 1]], 1, 7))