def solution(schedules, timelogs, startday):
    answer = 0
    # 출근 희망시각 + 10분까지 어플로 출근해야함.
    # 시각은 0000 으로 표기되며 100으로 나눈 몫이 시간, 나머지가 분이 된다.
    
    for e, schedule in enumerate(schedules):
        hour, minute = int(schedule // 100), int(schedule % 100)
        minute += 10
        if minute >= 60:
            minute -= 60
            hour += 1
        limit = int(f"{hour}{minute:02d}")
        
        for day, log in enumerate(timelogs[e]):
            today = startday + day
            if today % 7 == 0 or today % 7 == 6:
                continue
            
            if log > limit:
                break
        else:
            answer += 1
    
    return answer

print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))