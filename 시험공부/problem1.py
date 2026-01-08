"""
Docstring for problem1
N명의 친구가 게임을한다.
원형 테이블에 앉아있고(0과 -1 이 연결.) 시계방향으로 1~n 까지 번호 매겨지며,
round robin방식으로 순회.
n번 친구로부터 시계방향으로 움직이고 다시 1번으로 옴.
게임 규칙.
1. n번 친구부터 시작. 
2. 시작  한 친구를 포함해서 시계방향으로 다음 k명 친구들을 선택.(원형으로 이동, 일부 친구들은 여러번 선택.)
3. 마지막 선택된 친구가 원형 테이블에서 나가고 게임에서 진다.
4. 테이블에 친구가 1명 이상 남아있다면 방금 진 친구의 시계방향의 친구부터 다시 2반계를 반복.
"""

def solution(n, k):
    answer = 0
    
    # 테이블 만들기 n명이 앉으며, 각각 자신의 자리번호에 해당하는 번호를 가짐.
    table = [i+1 for i in range(n)]
    table_out = [i+1 for i in range(n)]
    
    # 테이블의 사람이 모두 사라질때까지 반복.
    currnet_step = 1
    winner = 0
    while table:
        # 자신부터 세서 k 번째 사람이 나간다.
            
        next_step = currnet_step+k-1
        
        # next step이 전체길이보다 길면 한바퀴 돌아서 다시 1번으로 돌아온다.
        while next_step >= n: 
            next_step = next_step - n
        
        if winner != 0:
            winner = table.pop(table.index(winner)-1)
            
        if not table:
            break
        
        print(next_step)
        winner = table[next_step-1]
        currnet_step = next_step
        
        print(table)
        
        
    return winner

if __name__ == "__main__":
    print(solution(5,2))
    # print(solution(6,5))