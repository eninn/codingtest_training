def solution(citations:list):
    answer = 0
    
    # 전체 n편 논문중에서 h번 이상 인용된 논문이 h편 이상, 
    # 나머지 논문은 h번 이하로 인용되면,
    # 그때의 h최대값이 과학자의 h-index가 된다.
    # 논문인용수는 0회이상 10,000회 이하.

    n = len(citations)
    
    citations.sort(reverse=True) # 내림차순 정렬
    
    for i, c in enumerate(citations):
        h = i + 1 # h는 현재까지 검사한 논문의 편수 논문의 편수.
        if h >= c: # 현재 논문의 인용횟수가 현재까지의 논문 편수보다 작아지는 경우 그 직전의 논문 편수가 최대 h-index
            return i
        
    return len(citations) # 위 작업을 모두 완료해도 통과한다면 논문 전체의 편수가 h-index가 된다.
    
print(solution([3, 0, 6, 1, 5]))