import sys
sys.setrecursionlimit(10**6)

def solution(n):
    
    answer = []
    
    
    # 입력 n 에 대해서 올바른 괄호조합.
    # 괄호는 오름차순으로 정렬해서 리턴.
    # n쌍 괄호에 대한 모든 괄호 조합을 생성해야함.
    
    dfs("", 0, 0, n, answer)
    
    
    
    
    return sorted(answer)
    
def dfs(result:str, left:int, right:int, n:int, answer:list):
    if left == n and right == n:
        answer.append(result)
        return
            
    # if left <= n and right <= n:
    #     dfs(result+"(", left+1, right, n, answer)
    #     if left >= right:
    #         dfs(result+")", left, right+1, n, answer)
    # else:
    #     return
    
    if left <= n:
        dfs(result+"(", left+1, right, n, answer)
        if right <= n and right < left:
            dfs(result+")", left, right+1, n, answer)
            
    else:
        return
if __name__ == "__main__":
    print(solution(3))