def solution(n, times:list):
    # 한심사대에는 동시에 한명만 처리가능하다.
    # 가장 앞의 사람이 빈 심사대에서 심사 -> queue사용?
    # 더 빨리 끝나는 심사대가 있다면 기다렸다가 그곳으로 갈 수 있다.
    # 모든 사람이 심사받을 때 걸리는 시간의 최소값을 리턴 -> 특정값 X일때 조건을 만족하는지 확인. -> 이분탐색 접근
    
    times.sort()
    
    left = times[0]
    right = times[-1] * n
    
    while left <= right:
        mid = (right + left) // 2
        
        total = sum([mid // x for x in times])
    
        # 심사받을 사람 수가 처리수 보다 적을때: 시간이 충분하거나 남음 -> right를 줄임.
        if total >= n:
            right = mid -1
        # 심사받을 사람수가 더 많을때: 시간이 부족함 -> left를 늘림
        else:
            left = mid + 1
        
    answer = left
    
    return answer
    