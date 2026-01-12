"""
Docstring for 코드챌린지.홀짝트리
루트노드가 없는 1개 이상의 트리가 있고 모든 노드는 서로 다른 번호를 갖고있다. 트리는 여러개이고 이를 포레스트라고 한다.
각 노드는 '홀수노드', 짝수노드, 역홀수노드, 역짝수 노드 중 하나.
각 트리에 대해서 '루트노드'를 설정했을 때, 홀짝 트리가 될수있는 트리 개수와 역홀짝트리가 될수있는 트리 개수를 구하려고한다.
nodes는 포레스트의 노드 번호를 담은 1차원정수배열이며, edges는 간선들의 정보를 담은 2차원 정수배열이다.

노드는 어디가 루트인지에 따라서 자식수가 변하지만, 연결된 간선 수는 변하지 않는 고정값이다.
즉 특정 노드에 대해서 노드번호%2==간선수%2(홀짝성질) / 노드번호%2 != 간선수%2(역홀짝성질)
한 트리가 홀짝트리가 되려면 단하나의 노드만 홀짝노드이며(루트노드), 나머지는 모두 역홀짝 노드여야한다(나머지노드는 부모가 하나씩 있어야하므로.)
 
"""
from collections import deque

def solution(nodes, edges):
    answer = [0,0]
    degrees_for_nodes = {node_id: [] for node_id in nodes}
    
    # 모든 노드의 차수 계산.
    for u,v in edges:
        degrees_for_nodes[u].append(v)
        degrees_for_nodes[v].append(u)
            
    # BFS 사용하여 연결된 트리 탐색
    # visited = [False for _ in range(len(nodes))]
    visited = {node_id: False for node_id in nodes}
    
    def bfs_searching_tree(start_node, visited):
        visited[start_node] = True
        case1, case2 = 0, 0
        
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            # case1: 홀짝성질: 노드번호%2 == 간선수%2
            degree = len(degrees_for_nodes[node])
            if node % 2 == degree % 2:
                case1 += 1
            else:
                case2 += 1
            
            for next_node in degrees_for_nodes[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
            
        return case1, case2
    
    for node in nodes:
        if not visited[node]:
            case1, case2 = bfs_searching_tree(node, visited)
        
            if case1 == 1:
                answer[0] += 1
            if case2 == 1:
                answer[1] += 1
    
    
    return answer
