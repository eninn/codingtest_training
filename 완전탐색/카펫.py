import math

def solution(brown, yellow):
    answer = [0, 0]
    # brown은 테두리의 개수
    # yellow는 테두리로 둘러쌓인 내부 격자의 개수
    # 총 크기는 brown + yellow
    # 가로 길이는 세로보다 같거나 길다.
    # 가로 세로의 길이는 격자의 총개수의 공약수 중에서 크기 차이가 가장 적게 나는 수들로 구성.
    all = brown + yellow
    w, h = 0, 0
    for i in range(1, int(math.sqrt(all)+1)):
        if all % i == 0:
            h = i
            w = all // i
            if yellow == (w - 2) * (h - 2):
                return [w, h]
    
    return answer

print(solution(24,24))