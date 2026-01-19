from itertools import combinations

def solution(line):
    answer = []
    # 직선 Ax + By + C = 0 으로 표현되는 n개의 직선 line은 [A, B, C] 정보가 담김.
    # A=0 이면서 B=0인 경우는 없음.
    # 겹치는 직선은 없음.
    # 별이 한개 이상 그려지는 입력만 주어짐.
    # 정수로만 표현되는 교점의 좌표를 표현해야함.
    # 두 직선의 교점이 유일하게 존재할경우 교점의 알고리즘이 주어짐.
    two_line = combinations(line, 2)
    
    cross_points = []
    for line1, line2 in two_line:
        x, y = cross_algorithm(line1, line2)
        if x == None:
            continue
        
        if x%1 == 0 and y%1 == 0:
            cross_points.append((int(x),int(y)))
        
    cross_points.sort(key=lambda x:(x[0], x[1]))

    max_x = max([x for x, y in cross_points])
    max_y = max([y for x, y in cross_points])
    min_x = min([x for x, y in cross_points])
    min_y = min([y for x, y in cross_points])
    
    result = [["."]*(max_x-min_x) for x in range((max_y-min_y))]
    
    for point in cross_points:
        result[point[1]][point[0]] = "*"
        
    for r in result:
        ans = "".join(r)
        answer.append(ans)
        
    return answer

def cross_algorithm(line1, line2):
    A, B, E = line1
    C, D, F = line2
    if (A*D - B*C) == 0:
        return None, None
    
    x = (B*F - E*D) / (A*D - B*C)
    y = (E*C - A*F) / (A*D - B*C)
    
    return x, y
    

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))

print(3%1)