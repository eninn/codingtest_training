"""
카카오 2019 기출문제.
친구가 아닌 사람과 대화할때, 본래 닉네임이 아닌 가상 닉네임을 사용하여 채팅방에 들어갈 수 있다.
오픈채팅방을 개설했을때 사용할 관리자 창을 만든다.
채팅방에서 닉네임 변경 방법.
    1. 채팅방을 나간 후 새로운 닉네임으로 다시 들어간다.
    2. 채팅방에서 닉네임 변경.
    닉네임을 변경하면 채팅방의 출력 메세지의 닉네임이 전부 변경된다. 
    채팅방을 나간 후 변경하거나, 들어온다음 변경해도 기존 기록의 문자열이 바꾼 닉네임으로 변경된다. 
중복 닉네임을 허용한다. -> 몇번째로 들어온 사람인지 고유 번호가 필요하다.(유저 아이디: 닉네임 딕셔너리를 관리한다)
"""

def solution(record):
    answer = []
    
    user_dict = {}
    status_check = []
    
    for rec in record:
        record_info = rec.split(" ")
        
        if record_info[0] == "Enter":
            user_dict[record_info[1]] = record_info[2]
            status_check.append((record_info[0], record_info[1]))
        elif record_info[0] == "Leave": # Leave 일때 len(record_info) == 2
            status_check.append((record_info[0], record_info[1]))
        elif record_info[0] == "Change":
            user_dict[record_info[1]] = record_info[2]
            
    for status, user_id in status_check:
        if status == "Enter":
            answer.append(f"{user_dict[user_id]}님이 들어왔습니다.")
        elif status == "Leave":
            answer.append(f"{user_dict[user_id]}님이 나갔습니다.")
            
    return answer

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))