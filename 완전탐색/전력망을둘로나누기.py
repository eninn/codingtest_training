def solution(n, wires:list):
    # n개 송전탑이 전선으로 '트리형태'로 연결.
    # 전선중 하나를 끊어서 네트워크를 2개로 분할.
    # 분할된 네트워크 수가 비슷하게 맞춰야함.
    # 두 전력망의 송전탑 갯수의 차이를 리턴
    # wires [[송전탑1, 송전탑2]] 연결을 의미함. 1<=송전탑1<=송전탑2<=n으로 구성
    # wires중 하나를 끊었을때 두개의 네트워크의 송전탑 갯수를 확인해서 그 차이가 제일 적은 케이스를 리턴?
    answer = 100

    wires_adj = [[] for _ in range(n+1)]
    for wire in wires:
        wires_adj[wire[0]].append(wire[1])
        wires_adj[wire[1]].append(wire[0])
    
    def dfs_network_search(v, visited, wire_to_skip:list):
        visited[v] = True
        count = 1
        for neighber in wires_adj[v]:
            if (wire_to_skip[0] == v and neighber == wire_to_skip[1]) or \
                (wire_to_skip[1] == v and neighber == wire_to_skip[0]):
                    continue
            
            if not visited[neighber]:
                count += dfs_network_search(neighber, visited, wire_to_skip)
        return count
    
    for i in range(len(wires)):
        visited = [False for _ in range(n+1)]
        res = dfs_network_search(1, visited, wires[i])
        answer = min(answer, abs(res*2 - n))
        
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))