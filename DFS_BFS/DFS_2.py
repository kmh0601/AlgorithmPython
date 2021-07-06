N,M = map(int,input().split())
maze = []

for i in range(N):
    maze.append(list(map(int,input())))

count = 0

def DFS(maze, x, y):

    if maze[x][y]:
        maze[x][y] = 0
        global count
        count += 1

        if x == N-1 and y == M-1:
            return 1
        else:
            if x < N-1:
                if DFS(maze,x+1,y):
                    return 1
            if y < M-1:
                if DFS(maze,x,y+1):
                    return 1
            if y > 0:
                if DFS(maze,x,y-1):
                    return 1
            if x > 0:
                if DFS(maze,x-1,y):
                    return 1

DFS(maze,0,0)
print(count)