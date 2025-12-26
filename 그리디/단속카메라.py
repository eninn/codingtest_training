# 프로그래머스 단속카메라 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 12:08-12:35

"""
통행하는 모든 차량이 단속카메라를 1번은 만나도록 카메라를 설치하는 목표.
이동하는 차량 경로 routes가 매개변수로 주어짐.
routes의 값 [a, b]는 차량의 이동 경로를 나타냄.
진입/진출 시점에서 카메라가 위치해도 만난것으로 간주함.
"""

def solution(routes):
    answer = 0
    
    # 경로를 오름차순으로 정렬
    routes = sorted(routes, key=lambda x:x[1])
    # 가장 가까운 경로부터 확인하면서 해당 경로의 진출위치(route[1])보다 작은 시작경로가 있는지 확인.
    # 한번이라도 해당 경로에 잡히면 해당경로는 제외해도 됨.
    # 현재 카메라의 위치도 함께 기록?
    camera_pos = -30001 # 최소 진입지점.
    
    for route in routes:
        if route[0] <= camera_pos:
            continue
        else:
            camera_pos = route[1]
            answer += 1
    
    return answer


if __name__ == "__main__":
    print(solution([[-20,-15], [-19, -16], [-14,-5], [-18,-13], [-5,-3]]))