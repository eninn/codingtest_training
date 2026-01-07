"""
카카오 2023 기출문제.
고객 약관동의를 얻어 수집된 1~n번까지의 개인정보 n개가 있음.
약관 종류는 여러가지이며, 약관마다 개인정보 보관 유효기간이 정해져있다. -> 약관 종류에 따른 유효기간이 정해져있음.
유효기간이 지나면 파기해야한다.
모든 달은 28일 까찌 있다고 가정한다.
개인정보가 수집된달+약관유효기간-1일 만큼만 보관 가능하며, 당월 당일에는 파기해야한다.
"""


def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    today_y, today_m, today_d = today.split(".")
    today = int(f"{int(today_y):04d}{int(today_m):02d}{int(today_d):02d}")
    print(today)
    for term in terms:
        terms_case, terms_priod = term.split(" ")
        terms_dict[terms_case] = int(terms_priod)
        
    for i, privacy in enumerate(privacies):
        
        if check_privacies_date(terms_dict, privacy) < today:
            answer.append(i+1)
        print(check_privacies_date(terms_dict, privacy))
    

    return answer


def check_privacies_date(terms_dict:dict, privacy:str):
    # 약관과 계약정보를 비교하여 만료일자를 계산한다.
    contrect_date, contrect_term = privacy.split(" ")
    
    year, month, day = contrect_date.split(".")
    year = int(year)
    month = int(month)
    day = int(day)
    
    month = month + terms_dict[contrect_term]
    while month > 12:
        year = year + 1
        month = month - 12
        
    day -= 1
    if day == 0:
        day = 28
        month -= 1
        if month == 0:
            year -= 1
            month = 12
            day = 28
    
    return int(f"{year:04d}{month:02d}{day:02d}")
        

if __name__ == "__main__":
    print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))