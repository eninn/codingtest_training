import heapq

def solution(operations:list):
    
    max_heap = []
    min_heap = []
    n = len(operations)
    visited = [False for _ in range(n)]
    
    for i, operation in enumerate(operations):
        order, num = operation.split(" ")
        num = int(num)
        
        if order == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
            
        elif order == "D":
            if num == 1:                
                clear_heap(max_heap, visited)
                
                if max_heap:
                    val, idx = heapq.heappop(max_heap)
                    visited[idx] = False
                    
            elif num == -1:              
                clear_heap(min_heap, visited)           
                
                if min_heap:
                    val, idx = heapq.heappop(min_heap)
                    visited[idx] = False
                    
    
    clear_heap(max_heap, visited)
    clear_heap(min_heap, visited)
                    
    if not max_heap or not min_heap:
        return [0, 0]
    else:
        return [-(max_heap[0][0]), min_heap[0][0]]
    
def clear_heap(heap, visit_list):
    while heap and not visit_list[heap[0][1]]:
        heapq.heappop(heap)
    
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))