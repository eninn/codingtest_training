"""
Docstring for 코드챌린지.서버증설회수
m명 늘어날때 서버 1대 추가.
한번 증설된 서버는 k시간동안 운영되며 이후 반납됨.
하루동안 모든 게임 이용자가 게임을 하기위해 게임서버를 증설해야하는 최소 횟수가 궁금함.
기본서버 1대가 주어짐.
매 시간마다 게임 이용자수를 확인할 수 있으며, 이때 증설된 서버 수에 따라서 서버를 추가해야할지 안해도 되는지 판단이 가능하다.
서버가 한번 증설되었다면 해당 서버가 줄어드는 시점은 k 시점 이후이다. 
따라서 증설된 서버와 k를 기준으로 증설된 서버가 다시 반납되는 로직을 만들어야한다.
"""
from collections import deque


def solution(players, m, k):
    answer = 0
    
    n = 0 # n은 증설한 서버수 기본적으로 1개의 서버가 제공된다. 서버당 이용자 커버수 는 (n+1)*m
    # return_time = [] # 서버가 증설되면 return해야할 시점을 힙큐로 저장한다. 가장 빠른 시간부터 처리해야하므로 힙큐로 구성했다.
    # 사실 추가되는 시간은 항상 이전에 추가된거보다 빠르므로 heapq말고 deque를 사용해도 문제가 없다.
    return_times = deque([])
    for t, player in enumerate(players):
        # t는 시각을 나타낸다. 시각이 0부터 시작하므로 그대로 사용 가능하다.
        # 먼저 증설된 서버가 제거되는 타이밍을 확인한다 제거된 시점에 서버가 부족하면 다시 증설해야하기 때문.
        while return_times:
            if return_times[0] > t:
                break
            else:
                return_times.popleft()
                n -= 1
                    
        while player >= (n+1)*m: # 사용자 수가 서버의 총 커버수를 넘으면 커버 가능할때까지 서버를 증설해야한다.
            return_time = t + k
            return_times.append(return_time)
            n += 1
            answer += 1
            
    return answer

print(solution([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5))