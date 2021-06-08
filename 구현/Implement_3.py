spot = list(input())
spot = list(map(ord, spot))
count = 0

# 방향 벡터
vector = [[1, -2],
[-1,-2],
[1,2],
[-1,2],
[2,-1],
[2,1],
[-2,-1],
[-2,1]]


for i in vector:
    temp = [a+b for a,b in zip(spot,i)]
    if temp[0] < ord('h') + 1 and temp[0] > ord('a') - 1 and temp[1] < ord('9') and temp[1] > ord('0'):
        count += 1
print(count)
