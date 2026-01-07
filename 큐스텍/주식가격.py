def solution(prices):
    answer = [0 for _ in range(len(prices))]
    idx_stack = []
            
    for i, price in enumerate(prices):        
        while idx_stack and prices[idx_stack[-1]] > price:         
            pop_idx = idx_stack.pop()
            answer[pop_idx] = i - pop_idx
        idx_stack.append(i)
        
    while idx_stack:
        idx = idx_stack.pop()
        answer[idx] = len(prices) - idx -1
        
    return answer