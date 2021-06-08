x, y = 1, 1
N = int(input())
trip = input().split()

#방향벡터
dx = [0,1,0,-1]
dy = [1,0,-1,0]
move = ['R','D','L','U']

for ch in trip:
    for i in range(len(move)):
        if ch == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x = nx
    y = ny
print(x,y)