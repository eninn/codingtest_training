def solution(sizes):
    answer = 0
    # 모든 명함의 가로 세로 길이 리스트. [[w, h]]
    # 가로-세로 는 눕혀서 수납할 수 있다.
    
    w_max = 0
    h_max = 0
    
    for size in sizes:
        # w를 항상 큰 값으로 두면 항상 너비가 크게 배치할 수 있으므로 이후 비교에서 편하다.
        if size[1] > size[0]:
            w, h = size[1], size[0]
        else:
            w, h = size[0], size[1]
            
        if w_max == h_max == 0:
            w_max = w
            h_max = h
            continue
        
        w_max = max(w_max, w)
        h_max = max(h_max, h)            
        
                
    print([w_max, h_max])
    answer = w_max * h_max
    
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))