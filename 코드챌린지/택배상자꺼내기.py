"""
Docstring for 코드챌린지.택배상자꺼내기
촉 택배수 n에 대해서 w 너비만큼 쌓아나가며, 홀수층일때는 정방향 짝수층일때는 역방향으로 숫자를 정렬한다.
꺼내야하는 택배번호 num에 대해서 위에서부터 택배를 하나씩 꺼내가면서 숫자 num까지 도달해야 한다.
num을 포함해서 꺼낸 상자의 개수를 리턴해야한다.
"""


def solution(n, w, num):
    answer = 0
    # 택배가 꽉차게 쌓인 층수 floor 는 n // w + 1 이다.
    floor = n // w 

    # last = n % w 가 0 이 아니라면 제일 높은 층에는 last 만큼 상자가 더 쌓여있어야한다.
    last = n % w
    if last > 0:
        floor += 1 # 마지막층이 있을 경우 1층이 추가된다.
    # 마지막층이 홀수층이라면 정방향, 짝수층이라면 역방향으로 last 수 만큼 택배가 쌓여있다.
    if last == 0:
        last_floor_filled = [True for _ in range(w)]
    else:
        last_floor_filled = [False for _ in range(w)]
        for i in range(last):
            if floor % 2 == 1:
                last_floor_filled[i] = True
            else:
                last_floor_filled[w-i-1] = True
    print(last_floor_filled)
    # num의 위치는 w로 부터 확인할 수 있다.
    num_floor = num // w # 3
    num_last = num % w # 0
    if num_last > 0:
        num_floor += 1
    # num_lv의 홀짝에 따라서 왼쪽 혹은 오른쪽부터 num_last 위치 만큼 이동한곳이 꺼내야할 상자의 위치이다.
    if num_last == 0:
        num_last = w
    if num_floor % 2 == 1:
        num_pos = num_last - 1
    else:
        num_pos = w - num_last
        
    # 먼저 마지막층을 고려하지 않고 자기자신을 포함해서 제거해야할 택배상자 수를 계산한다.
    answer = (floor - 1) - (num_floor - 1) # 전체층수에서 제일 상층을 제회한 층수 - 자신까지 제거하고 남은 층수
    
    # 자신의 위치를 기준으로 last_floor_filled 가 채워져있는지 확인하고, 채워져있다면 answer += 1
    if last_floor_filled[num_pos]:
        answer += 1        

    return answer

print(solution(4, 1, 2))