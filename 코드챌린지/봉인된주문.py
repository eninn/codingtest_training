"""
Docstring for 코드챌린지.봉인된주문
각 주문은 알파벳 소문자 11글자 이하로 구성되어있고, 실제로 효과가 없는 주문의 작성 순서가 있다.
주문의 순서는
1. 근자수가 적은 주문부터 먼저 기록.
2. 글자수가 같다면 사전 순서대로 기록. (단순 sort로 는 정렬 안됨)
삭제된 주문 리스트는 제외하고 n번째 주문이 탐색되어야함.
n번째 주문을 탐색해야하고 삭제된 주문 리스트를 bans에 담아서 입력될때 삭제완료된 주문서의 n번째 주문을 return
n <= 10**15
bans <= 300k
1 <= 문자열길이 <= 11
케이스가 매우 많으므로 순서대로 세면서 제거되야하는 주문을 제외하고 수를 세야할 것 같다.
매 작업마다 bans를 확인하는것은 너무 비효율적이다.
알파벳으로 이루어진 문자를 26진수숫자라고 생각하고 계산해본다.
"""

def spel_to_num(spel):
    n = len(spel)
    num = 0
    # 자리수에 따른 숫자보정
    for i in range(1, n):
        num += 26**i
    # 현 자리수에서 몇번째인지 확인
    for i in range(n):
        a_to_n = ord(spel[n-1-i]) - 96
        num += 26**i * (a_to_n -1)
    num += 1 
    return num

def num_to_spel(num):
    order = 1
    spel = ""
    while num > 26**order:
        num -= 26**order
        order += 1 
        
    num -= 1
    for i in range(order, 0, -1):
        index = (num // 26**(i-1))
        n_to_a = chr(index + 97)
        num = num % 26**(i-1)
        spel += n_to_a
    
    return spel
    

            
def solution(n, bans:list):
    
    numed_bans = [spel_to_num(s) for s in bans]
    numed_bans.sort()
    
    for ban in numed_bans:
        if ban <= n:
            n += 1
        else:
            break
    
    answer = num_to_spel(n)
    
    
    return answer


# x=['a', 'b', 'ba', 'czzz', 'daaa', 'aa', 'az', 'aba', 'aaz', 'aab', 'abaa']
# x.sort()
# print(x)


# x.sort(key=cmp_to_key(ordering))
# print(x)

print(solution(30, ["d", "e", "bb", "aa", "ae"]))