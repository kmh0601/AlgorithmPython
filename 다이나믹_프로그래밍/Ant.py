n = int(input())
food = list(map(int,input().split()))
visited = [-1]*n

def Food(visited, food):
    while -1 in visited:
        max = 0
        index = 0
        jndex = 0
        for i in range(len(food)):
            temp = food[i]
            if visited[i] != -1:
                continue
            for j in range(len(food)):
                if visited[j] != -1 or j == i-1 or j == i+1:
                    continue
                if j == i:
                    temp = food[i]
                else:
                    temp = food[i]+food[j]
                if max < temp and visited[i] != False and visited[j] != False:
                    max = temp
                    index = i
                    jndex = j
        visited[index], visited[jndex] = True, True
        if index == 0:
            visited[index + 1] = False
        elif index == len(food)-1:
            visited[index - 1] = False
        else:
            visited[index + 1], visited[index - 1] = False, False

        if jndex == 0:
            visited[jndex+1] = False
        elif jndex == len(food) - 1:
            visited[jndex - 1] = False
        else:
            visited[jndex + 1], visited[jndex - 1] = False, False
        print(visited)

Food(visited,food)
result = 0
for i in range(len(food)):
    if visited[i] != False:
        result += food[i]
print(result)