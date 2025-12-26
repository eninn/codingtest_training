# 프로그래머스 구명보트 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 10:53-11:13

"""
구명보트는 한번에 최대 2명 탑승하며, 무게제한 limit이 있다.
구명보트 를 최대한 적게 사용하면서 모든 사람을 구출하자.
사람을 2명씩 더하는데, 이때 limit이 통과 될때까지 가능한 사람을 확인하고, 없으면 그사람만 태워서 보낸다.
"""

def solution(people:list, limit:int):
    answer = 0
    
    # 사람을 적은 몸무게순으로 확인.
    people.sort()
    
    left, right = 0, len(people)
    
    while left < right:
        if people[left] + people[right-1] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
        
    # 마지막 한명 탑승
    return answer
        
if __name__ == "__main__":
    print(solution([70, 50, 80, 50], 100))
    print(solution([70, 80, 50], 100))