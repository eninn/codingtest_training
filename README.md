# 코딩테스트 연습문제 모음

## 프로그래머스
### 깊이/너비 우선탐색(DFS/BFS)
https://school.programmers.co.kr/learn/courses/30/parts/12421    

* BFS: queue와 while 문을 사용하여 조건에 맞는 가장 빠른 경우를 탐색한다. `from collections import deque` 를 사용한다   
* DFS: 재귀함수를 사용하여 탐색 조건이 종료될 때 까지 계속 반복해 들어간다. 답 정보를 외부로 전달하기위한 list 또는 global 변수를 사용한다. `sys.setrecursionlimit(10**6)` 를 사용하여 재귀 제한을 풀어준다.   

### 탐욕법(Greedy)
https://school.programmers.co.kr/learn/courses/30/parts/12244   
모든 케이스를 탐색하는 경우에서 left/right 포인터 등을 활용하여 탐색 케이스를 최소화하는 로직을 사용한다.   
* 최소신장트리-크루스칼 알고리즘: Find, Union 함수를 설계하고 부모노드를 탐색하여 모든 노드를 하나의 트리로 만드는 기법.   

### 해시(Hash)
https://school.programmers.co.kr/learn/courses/30/parts/12077    
입력값에 대한 고유값을 구분할 수 있어야한다. 공통되는 값을 가지는 요소들을 묶어 `dictionary` 로 자료구조를 정리하고 활용한다.   

### 동적계획법(DP)
https://school.programmers.co.kr/learn/courses/30/parts/12263    
작은 문제들을 결합하여 큰문제를 풀어낸다.   
처음부터 끝까지 연산해야하는 케이스에서 이전 연산의 결과를 다음 연산에 활용하여 연산량을 최소화한다. (결과 누적 기법)   
누적 값을 리스트에 저장하여 관리하는 기법을 활용한다.   
