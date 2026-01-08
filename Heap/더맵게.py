import heapq

def solution(scoville:list, K:int):
    answer = 0
    heapq.heapify(scoville)
        
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        lower_food = heapq.heappop(scoville)
        second_lower_food = heapq.heappop(scoville)
        
        new_food = lower_food + second_lower_food*2
        
        heapq.heappush(scoville, new_food)
        answer += 1
        
    return answer
    
print(solution([1, 2, 3, 9, 10, 12], 7))