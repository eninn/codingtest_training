def solution(price, money, count):
    answer = -1
    
    total = 0
    for i in range(1, count+1):
        total += i
    payed_price = price * total
    answer = payed_price - money
    if answer <= 0:
        answer = 0

    return answer