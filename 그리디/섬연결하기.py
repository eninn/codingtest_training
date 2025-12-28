# 프로그래머스 섬 연결하기 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 11:26-12:08

"""
섬 연결 시 n 개 섬과 다리 건설 비용이 주어진다.
최소의 건설 비용으로 모든 섬을 통행해야한다.
다리를 여러번 건너도 되며 섬끼리 연결만 되면 됨.
cost[0], cost[1] 연결되는 다리 번호, cost[2] 비용.
비용이 적은 순서대로 다리들을 연결하면서 모든 다리가 연결될 수 있는지 확인해봐야함.
가장 적은 비용부터 순서대로 먼저 다 연결. 그다음 연결이 부족한 부분을 채운다.
최소 신장 트리 - 크루스칼 알고리즘을 사용한다. 다리를 연결할때 연결된 섬을 다시 연결하지 않도록해야함.
유니온 파인드 자료구조를 활용함.
"""

def solution(n:int, costs:list):
    answer = 0
    
    costs = sorted(costs, key=lambda x:x[2])
    parent_island = [i for i in range(n)]

    
    # union-find 알고리즘 사용.
    # find 함수: parent 가 자신일때까지 반복해서 재귀함.
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    
    def union(parent, x, y):
        px = find(parent, x)
        py = find(parent, y)
        
        if px != py:
            parent[py] = px
    
    for cost in costs:
        if find(parent_island, parent_island[cost[0]]) != find(parent_island, parent_island[cost[1]]):
            answer += cost[2]
            union(parent_island, cost[0], cost[1])
    
    return answer

if __name__ == "__main__":
    print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))

    
    

    

