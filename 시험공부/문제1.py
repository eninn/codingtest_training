# 오늘의집 연습문제
"""
직사각형 4개가 주어지고 한점의 좌표 구하기.
직사각형을 만들때 필요한 4개 점중 3개 좌표가 주어질때 나머지 한점의 좌표를 구한다.
점 3개가 [x,y] 축 기준으로 2중리스트로 주어짐
나머지
"""
def solution(v):
    dict_x = {}
    dict_y = {}
    
    for x, y in v:
        if x not in dict_x:
            dict_x[x] = 1
        else:
            dict_x[x] += 1
        if y not in dict_y:
            dict_y[y] = 1
        else:
            dict_y[y] += 1
            
    for k, count in dict_x.items():
        if count == 1:
            x = k
            break
        
    for k, count in dict_y.items():
        if count == 1:
            y = k
            break
            
    return [x, y]

if __name__ == "__main__":
    print(solution([[1, 4], [3, 4], [3, 10]]))