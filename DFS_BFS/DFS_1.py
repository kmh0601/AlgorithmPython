N,M = map(int,input().split())

def DFS(visited,x,y,ice):
    if ice[x][y] != 1 and visited[x][y] != True:
        visited[x][y] = True
        # 오른쪽으로 먼저 탐색
        if y+1 < M:
           DFS(visited,x,y+1,ice)
        # 아래쪽으로 탐색
        if x+1 < N:
            DFS(visited,x+1,y,ice)
        '''
        if y-1 > -1:
            DFS(visited,x,y-1,ice)
        if x-1 > -1:
            DFS(visited,x-1,y,ice)
        '''
        #웬만하면 상하좌우를 다 체크하자


Visited = [[False for _ in range(M)]for _ in range(N)]
Ice = []
count = 0
i = 0
while i < N:
    Ice.append(list(map(int,input())))
    i += 1


for x in range(N):
    for y in range(M):
        if Ice[x][y] != 1 and Visited[x][y] != True:
            DFS(Visited,x,y,Ice)
            count += 1
print(count)