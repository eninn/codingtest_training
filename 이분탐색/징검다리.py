def solution(distance, rocks, n):
    # 출발점부터 distance만큼 떨어진 곳에 도착점이 있다. 그리고 사이에 바위들이 놓여있다.
    # 바위를 랜덤하게 n개 만큼 제거한다.
    # 제거하고 남은 바위들과 출발점,도착점 사이의 거리를 구하고, 해당 거리들의 '최소값'들중에서 가장 큰 값을 리턴해야한다.
    # 이분탐색으로 접근했을때, mid는 '유지하고싶은 바위 사이의 최소거리' 로 가정해야함.
    # 바위 사이의 거리들은 최소한 mid 이상을 유지해야한다.
    answer = 0
    
    rocks.sort()
    
    left = 1
    right = distance
    while left <= right:
        mid = (left + right) // 2 # mid 는 유지될 바위의 최소거리
        # mid를 만족하기 위해 바위를 몇개 제거해야하는지 확인.
        start_pos = 0
        removed_rock = 0
        for rock in rocks:
            if rock - start_pos < mid:
                removed_rock += 1
            else:
                start_pos = rock
        if distance - start_pos < mid:
            removed_rock += 1
        
        if removed_rock > n:
            right = mid - 1
        else:        
            answer = mid
            left = mid + 1
            
    
    return answer