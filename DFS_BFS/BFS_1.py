from collections import deque

#BFS는 간선의 가중치가 같은 그래프의 최단거리 탐색을 위한 알고리즘이다.
#큐에 위치들을 넣은 뒤에 차례로 꺼내서 현재위치로 삼고, 현재위치에서 이동할 수 있는 위치에다가 현재 위치의 가중치를 더하고 큐에 넣어준다.

def bfs(maze, x, y):
    # 큐 만들기
    queue = deque()
    # 튜플 형식으로 시작 위치 넣어주기
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치 꺼내기

        #### 이 부분 잘 응용해보자. 자주 쓰이는 형태 :  nx, ny로 임시 위치 만들어주고 규격 넘는지 확인하고 대입 ###
        ## 이때 방향벡터와 반복문을 이용해 코드 간략화 ##
        for i in range(4):
            #이동할 위치(사방향)
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                #미로의 규격을 넘는다면
                continue
            if maze[nx][ny] == 1:
                # 만약 벽이 아니라면 이동할 위치는 현재위치에서 1을 더한 값을 가진다
                maze[nx][ny] += maze[x][y]
                # 이동한 위치는 다시 큐에 넣어준다
                queue.append((nx,ny))
    return maze[n-1][m-1]

n, m = map(int,input().split())

maze = []
for i in range(n):
    maze.append(list(map(int,input())))

#이동 벡터 -> 우좌하상
dx = [0,0,1,-1]
dy = [1,-1,0,0]

print(bfs(maze, 0, 0))