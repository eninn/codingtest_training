# 프로그래머스 큰 수 만들기 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 10:10-10:53
"""
어느 숫자에서 k개의 수를 무조건 제거해야하며, 이때 얻는 수중에서 가장 큰수를 구한다.
문자열 형식으로 숫자 number가 제공되고 제거해야하는 수 k 가 함께 제공됨.
k는 number 자리수 미만으로 들어옴.
"""
def solution(number:str, k:int):
    answer = []
    
    
    number_list = list((number))
    number_list.reverse()
    
    while k > 0:
        if not number_list:
            break
        current_num = number_list.pop()
        
        if not answer:
            answer.append(current_num)
            continue            
        else:
            while answer:             
                if k <= 0:
                    break
                if int(current_num) <= int(answer[-1]):
                    break
                else:
                    answer.pop()
                    k -= 1                    
            answer.append(current_num)
                
    number_list.reverse()
    
    answer.extend(number_list)
    if k > 0:
        answer = answer[:-k]
    
    return "".join(answer)
    
    
if __name__ == "__main__":
    print(solution("4177252841", 4))