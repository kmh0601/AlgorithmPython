N = int(input())
array = list(map(int,input().split()))

# array.sort(reverse = 1 )
# 공포도가 큰 순서로 그룹을 나누어주면 최대값이 나올 수 없는 경우가 있음
# 극단적으로 5 2 2 2 2 1 이 있을때, (2 2),(2 2),1 이 나올게 (5 2 2 2 2 )
# 가 될 수 있기 떄문이다.
# 이처럼 최대한(그룹핑문제 등) -> 작은거부터 / 최소한(동전문제 등) -> 큰거부터 잘 기억해두자
i = 0
count = 0

while i != N:
    temp = i + array[i]
    if temp > N:
        i += 1
    else:
        i = temp
        count += 1

print(count)
