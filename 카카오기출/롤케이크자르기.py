"""
코딩테스트 연습문제. 132265
롤케이크를 두조각으로 잘라 동생과 한조각씩 나눠먹으려한다.
여러 토핑들이 일렬로 올려져있고, 롤케익을 공평하게 나눠먹고 싶은데 크기보다 토핑 종류가 공평해야한다.
동일 가지수의 토핑이 올라가면 공평하게 롤케이크가 나눠진것으로 판단한다.
자르기는 한번밖에 못한다.
한번 잘랏을때 양쪽의 토핑 종류(숫자)의 갯수가 최소가 되는 idx를 저장해야한다.
양쪽 리스트의 토핑종류만 보면 되므로 set을 사용하여 중복을 제거하고 토핑 종류만 확인한다.
중앙서부터 시작해서 위 아래로 옮기는 방법?
"""
from collections import Counter

def solution(topping:list):
    answer = 0 # 공평하게 나눌수없을때 0을 리턴한다.
    
    right_dict = Counter(topping)
    right_topping_num = len(right_dict)
    left_set = set()
    left_topping_num = 0
            
    for t in topping:
        if t not in left_set:
            left_set.add(t)
            left_topping_num += 1
            
        right_dict[t] -= 1
        if right_dict[t] == 0:
            right_topping_num -= 1
            
        if right_topping_num == left_topping_num:
            answer += 1
        if right_topping_num < left_topping_num:
            break

        
    return answer

    

if __name__ == "__main__":
    print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
    print(solution([1, 2, 3, 1, 4]))