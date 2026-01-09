from itertools import permutations

def solution(k:int, dungeons:list):
    answer = 0
    # 최소피로도: 탐험을 위한 최소한의 피로도
    # 소모피로도: 탐험 후 소모되는 피로도
    # 현재피로도 k, [최소피로도, 소모피로도] 리스트 가 주어짐. 
    # 최대 던전 탐험 수를 리턴.
    # 최소피로도가 큰 수, 소모피로도가 작은 순서대로 재정렬.
    # 던전이 최대 8개 이므로 모든 순서를 확인하고 몇개나 돌수 있는지 확인(순열)
    n = len(dungeons)
    clear_cases = []
    # 모두 나열했을때의 케이스
    clear_cases.extend(list(permutations(dungeons, n)))
    
    # 각 케이스를 확인하면서 소모된 피로도를 차감하고 카운트를 늘리면서 max count를 확인한다.
    for clear_case in clear_cases:
        clear_k = k
        count = 0
        for dungeon in clear_case:
            if clear_k < dungeon[0]:
                break
            clear_k -= dungeon[1]
            count += 1
        answer = max(answer, count)
    
    return answer

print(solution(80,  	[[80,20],[50,40],[30,10]]))