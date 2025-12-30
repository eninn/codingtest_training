"""
카카오 2022 기출문제
나만의 성격유형 검사지를 만들려고 한다.
4개의 지표로 성격을 구분하고 각 지표당 2개의 유형중 하나로 결정된다.
성격 유형은 총 16가지가 가능하다.
검사지는 n개의 질문과 7개의 선택지가 있다.
각 질문은 1가지 지표로 성격 유형 점수를 판단한다.
약간동의/비동의 1점, 동의/비동의2점, 매우동의/비동의 3점, 모르겟음 0점.
모든 질문의 성격유형 점수를 더하여, 각 지표의 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단한다.
survey의 원소는 7개 케이스로 들어온다.
survey와 choices의 수는 같으며 각 survey[i]에 대한 답변을 choice[i]에 기록한다.
비동의 일수록 survey[i][0]에 동의일수록 survey[i][1]에 점수를 추가한다.
점수가 동일하면 사전순으로 빠른 유형이 선택된다.
"""


def solution(survey, choices):
    answer = ''
    surv_score = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for surv, choice in zip(survey, choices):
        if choice == 0:
            continue
        if choice < 4:
            surv_score[surv[0]] += 4 - choice
        else:
            surv_score[surv[1]] += choice - 4
        
    # 점수에 따른 유형 선택.
    if surv_score["R"] >= surv_score["T"]:
        answer += "R"
    else:
        answer += "T"
    
    if surv_score["C"] >= surv_score["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if surv_score["J"] >= surv_score["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if surv_score["A"] >= surv_score["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer
    
