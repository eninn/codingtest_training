"""
Docstring for 그래프.방의개수
방을 이동하는 좌표가 제공됨.
그림을 그릴때 사방이 막혀있을경우 방 하나로 센다.
이동방향이 주어지는 arrows가 제공되며 방의 개수를 리턴해야한다.
방은 다른 방으로 둘러쌓여야한다.
문제를 '맵'문제로 보지말고 좌표가 이동되다가 이미 방문했던 지점을 만났을때 방이 완성된다는 점에 주의한다.
'방문했던 정점' 인 동시에 '이동한 간선이 처음 사용한것'일것인 경우 방이 완성된다.(동일한 간선을 따라서 이동할 수도 있음.)
'대각선'이 교차하는 상황에서도 방이 생길 수 있음. -> 이동을 2배수로 이동하면 중간의 교차점을 확인할 수 있음.
"""

dx = [ 0,  1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1,  1,  0, -1]

def solution(arrows):
    answer = 0
    
    nodes = set() # (좌표x, 좌표y)
    edges = set() # (출발x,출발y, 도착x, 도착y)
    
    node_now = (0, 0)
    nodes.add(node_now)
    
    for arrow in arrows:        
        for i in range(2): # 간선의 중간이 교차하는 부분을 고려하기 위해서 2배수 이동처리
            next_node = (node_now[0] + dx[arrow], node_now[1] + dy[arrow])
            edge = (node_now[0], node_now[1], next_node[0], next_node[1])
            edge_reverse = (next_node[0], next_node[1], node_now[0], node_now[1])
            
            if edge not in edges: # 이번 간선이 처음 이동되는 간선인 경우에만 판별.
                edges.add(edge)
                edges.add(edge_reverse)
            
                if next_node not in nodes: # 중간 노드가 방문노드에 없을 경우 방문 처리
                    nodes.add(next_node) 
                else: # 중간노드가 방문한 노드일 경우:
                    answer += 1
        
            node_now = next_node
                
            
    return answer
    