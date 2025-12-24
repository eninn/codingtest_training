# 프로그래머스 퍼즐 조각 채우기 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/8402
# 16:34-17:58

"""
테이블 퍼즐조각 맞추기. 조각을 한번에 하나씩 채워넣고, 회전시킬 수 있음.(뒤집기는 안됨)
게임보드에 채워넣은 퍼즐조각은 인접칸이 비어있으면 안됨.(즉 꽉채워야함.)
게임보드의 빈칸에 테이블의 조각을 넣어보면서 인접칸이 비지 않으면서 넣을수있는 경우의 수 중에서 가장 많은 칸을 채워넣는 로직을 만들기.
블록은 최대 6개까지 연결된 1X1 크기의 정사각형으로 구성됨.
최대한 많은 경우의수를 탐색 -> DFS 로직을 사용해야할 것으로 보임.
"""
from typing import List

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



def extract_piece(map:List[List[int]], visited_map:List[List[bool]], pieces:list, locate:int):
    # game_board: 빈공간 0 -> locate=0
    # table: 퍼즐조각 1 -> locate=1
    
    def bfs(piece:List[set], x:int, y:int):
        queue = [(x, y)]
        visited_map[x][y] = True
        if map[x][y] == locate:
            piece.append((x, y))            
            while queue:
                current_pos = queue.pop(0)            
                for i in range(4):
                    next_pos = (current_pos[0]+dx[i], current_pos[1]+dy[i])
                    if next_pos[0] < 0 or next_pos[0] >= len(map) or next_pos[1] < 0 or next_pos[1] >= len(map[0]):
                        continue
                    if visited_map[next_pos[0]][next_pos[1]]:
                        continue
                    if not visited_map[next_pos[0]][next_pos[1]] and map[next_pos[0]][next_pos[1]] == locate:
                        queue.append(next_pos)
                        visited_map[next_pos[0]][next_pos[1]] = True
                        piece.append(next_pos)
    
    # 모든 visited_map 이 false 인 상황을
    for i in range(len(map)):
        for j in range(len(map[0])):
            if not visited_map[i][j] and map[i][j] == locate: 
                piece = []            
                bfs(piece, i, j)
                pieces.append(piece)
            else: visited_map[i][j] = True        
            
def piece_locate_normalize(pieces:List[List[int]]):
    min_x = min(p[0] for p in pieces)
    min_y = min(p[1] for p in pieces)
    
    norm = sorted([(x-min_x, y-min_y) for x, y in pieces])
    
    return norm

def rotate_puzzle(pieces:List[List[int]]):
    # 90도 회전하려면 (x, y) -> (y, -x) 가 되어야함. 이후 다시 정규화를 통해 좌표를 0,0이 최소가 되도록 맞춰줌.
    rotated_pieces = []
    for x, y in pieces:
        rotated_pieces.append((y, -x))
    
    return piece_locate_normalize(rotated_pieces)
            

def solution(game_board:List[List[int]], table:List[List[int]]):
    answer = 0
    
    # 타일의 회전을 처리하려면 table 자체를 회전시켜서 해당 케이스들을 모두 확인하는 편이 빠를거같음.
    # 테이블에서 하나로 묶인 퍼즐들을 먼저 확인.
    # 퍼즐을 하나씩 확인하면서 게임보드에서 해당 퍼즐이 딱 맞는 위치가 있는지 탐색(퍼즐의 모든 블록의 상하좌우가 1 로 막혀있어야함.)
    # 퍼즐은 회전시키면서 케이스를 확인해야함-> 회전 로직?
    # 딱 맞는 위치를 찾으면 테이블에서 제거하고(제거된 수 만큼 answer 값 증가) 
    # 맞춤 종료 후 테이블에 퍼즐이 남아있으면 테이블을 90도 회전시킨다음 다시 맞는 위치를 탐색. 
    
    
    visited_game_board = [[False]*len(game_board[0]) for _ in range(len(game_board))]
    board_spaces = []
    extract_piece(game_board, visited_game_board, board_spaces, 0)
    normalized_board_spaces = [piece_locate_normalize(space) for space in board_spaces]
    # normalized_board_spaces =piece_locate_normalize(board_spaces)
    
    visited_table = [[False]*len(table[0]) for _ in range(len(table))]
    table_pieces = []
    extract_piece(table, visited_table, table_pieces, 1)
    normalized_table_pieces = [piece_locate_normalize(piece) for piece in table_pieces]
    # normalized_table_pieces = piece_locate_normalize(table_pieces)
    
    for piece in normalized_table_pieces:
        rotate_num = 0
        while rotate_num < 4:
            if piece in normalized_board_spaces:
                answer += len(piece)
                normalized_board_spaces.remove(piece)
                break
            else:
                piece = rotate_puzzle(piece)
                rotate_num += 1
    
    return answer

if __name__ == "__main__": 
    print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
                   [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))