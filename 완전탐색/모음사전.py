from itertools import permutations

def solution(word):
    # 사전의 단어는 AEIOU만 사용해서 만들수있고 최대길이 5로 이루어짐.
    # 모음 AEIOU로만 구성된 단어가 입력됨.
    #     123450
    # 첫단어는 A, 마지막단어는 UUUUU
    # 입력된 단어가 몇번째 단어인지 확인하는 함수 완성.
    # 각 자리수의 가중치: 5번: 1, 4번: 5번가중치*5+1, 3번: 4번가중치*5+1, ...
    # 5: 1, 4: 5*1+1, 3: 6*5+1=31, 4: 31*5+1=156, 5:156*5+1=781    
    answer = 0
    pos_weight = {5:1, 4:6, 3:31, 2:156, 1:781}
    vowels = "AEIOU"
    
    for i, chr in enumerate(word):
        pos = i+1
        vowel_idx = vowels.index(chr)
        count = vowel_idx*pos_weight[pos] + 1
        answer += count
    
    return answer

print(solution("AAAAE"))