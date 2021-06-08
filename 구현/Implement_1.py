N = int(input())
trip = input().split()

dx, dy = 1, 1

for ch in trip:
    if ch == 'U':
        if dx > 2:
            dx -= 1
    if ch == 'D':
        if dx < N:
            dx += 1
    if ch == 'R':
        if dy < N:
            dy += 1
    if ch == 'L':
        if dy > 2:
            dy -= 1
print(dx, dy)