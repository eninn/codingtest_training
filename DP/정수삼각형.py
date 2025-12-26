# 프로그래머스 정수삼각형 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 17:00-17:18

"""
삼각형꼭대기에서 바닥까지의 경로중에서 거쳐간 숫자의 합이 가장 큰 경우를 찾는다.
아래칸으로 이동할때는 대각선으로 한칸 오른쪽/왼쪽으로만 이동이 가능하다.
트리 형태에서 아래로 내려간다. 맨 마지막까지 탐색했을때의 총 합이 더 큰 경우를 선택해야한다.
삼각형을 이루는 숫자는 0~9999 이하의 정수이므로 맨 마지막에 역전되는 경우도 존재한다.
케이스들을 확인하면서 매 층마다 값을 갱신해 나가야 한다.
현재 층에서 계산할 값은 다음층의 자기자신의 번호 또는 다음번호만 더할 수 있다.
"""

def solution(triangle):
    answer = 0
    
    # 1층부터 순서대로 더한다.
    calcs = []
    for floor in triangle:
        # 아무것도 없는 경우
        if not calcs:
            calcs = floor
            continue
        
        for i in range(len(floor)):
            if i == 0:
                floor[i] += calcs[i]
            elif i == len(floor)-1:
                floor[i] += calcs[i-1]
            else:
                floor[i] += max(calcs[i-1], calcs[i])
        calcs = floor
                
    return max(triangle[-1])

if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))