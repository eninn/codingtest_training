import heapq

def solution(jobs): 
    n = len(jobs) 
    
    jobs.sort() # [시작시간, 작업시간]
    
    response_time = 0
    now = 0 # 현재 시각
    i = 0
    start = -1 # 직전작업 종료시간
    
    heap = []
    
    while i < n:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0])) # [작업시간, 시작시간] 순서대로 작업 처리
        
        # 한번에 최대 하나의 작업만 처리
        if heap:
            work_time, start_time = heapq.heappop(heap)
            start = now
            now += work_time
            response_time += (now - start_time)
            i += 1
        else:
            now += 1 # 작업 없을때 다음작업으로 시간 이동.
            
    return response_time // n
    
    
    
print(solution([[0, 3], [1, 9], [3, 5]]))