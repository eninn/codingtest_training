# 프로그래머스 폰켓몬 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 09:14-09:35
"""
포캣몬 N마리 중 N/2 마리 챙겨갈 수 있음. N은 항상 짝수.
같은 종류의 포캣몬은 같은 번호를 가짐.
최대한 많은 종류의 폰켓몬을 포함하여 N/2 마리를 선택해야함.
최대한 많이 골랐을때의 포켓몬 종류의 수를 리턴.
"""
from typing import List

def solution(nums:List[int]):
    answer = 0
    
    # 입력받은 폰켓몬 수를 딕셔너리로 구성.
    pokemon_dict = {}
    for p in nums:
        if p in pokemon_dict:
            pokemon_dict[p] += 1
        else:
            pokemon_dict[p] = 1

    pokemon_num = len(pokemon_dict.keys())
    # 전체 폰켓몬 길이 len(nums)/2 만큼 반복하면서 딕셔너리를 순서대로 돌면서 저장된 폰켓몬 수를 하나씩 제거. 
    # 특정 key에서 폰켓몬이 제거될때마다 answer 값을 하나씩 올리고 모든 폰켓몬 수만큼 되었으면 즉시 return
    cycles = len(nums) // 2
    poke_roop = list(pokemon_dict.keys())
    while cycles > 0:
        if not poke_roop:
            poke_roop =  list(pokemon_dict.keys())
        if answer == pokemon_num:
            return answer
        
        pokemon = poke_roop.pop()
        
        if pokemon_dict[pokemon] > 0:
            pokemon_dict[pokemon] -= 1
            answer += 1
        cycles -= 1
    
    return answer

def solution2(nums:List[int]):
    # 입력받은 폰켓몬 수를 딕셔너리로 구성.
    pokemon_dict = {}
    for p in nums:
        if p in pokemon_dict:
            pokemon_dict[p] += 1
        else:
            pokemon_dict[p] = 1
            
    pokemon_num = len(pokemon_dict.keys())
    maximum_pokemon = len(nums) // 2
    
    return min(pokemon_num, maximum_pokemon)
    
    
if __name__ == "__main__":
    print(solution([3,1,2,3]))