from collections import deque

def BFS(graph, start, visited):
    # 현재위치를 큐에 삽입
    queue = deque([start])
    # 현재위치를 방문완료로 등록
    visited[start] = 1

    # 큐가 빌때까지
    while queue:
        #큐에서 원소 하나 뽑기
        v = queue.popleft()
        print(v,end = ' ')
        #뽑은 원소의 인근 미방문 원소들 모두 큐에 넣기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

