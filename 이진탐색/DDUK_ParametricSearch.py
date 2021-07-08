n, m = map(int,input().split())
DDUK = list(map(int,input().split()))

# 0 ~ 최대 떡길이 => 절단기 크기의 범위
size = list(range(max(DDUK)+1))

def sum(mid):
    global DDUK
    result = 0
    for i in DDUK:
        if (i - mid) >= 0:
            result += (i-mid)
    return result

def BinarySearch(list, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        size = sum(mid)
        if size == target:
            return mid
        elif size < target:
            end = mid - 1
        else:
            start = mid + 1
    return end

print(BinarySearch(size,m,0,len(size)-1))

'''ParametricSearch는 최적화문제를 결정문제로 바꾸어 해결하는 기법이다.
   이때, 최적화 문제란 주어진 조건에 가장 적절한 값을 찾는 문제이고, 결정문제란 yes or no로 평가할 수 있는 문제를 말한다.
   즉, 이진탐색을 통해 x란 값을 도출하고 조건에 맞는지 yes or no를 진행하고 다시 한 번 x의 좌범위 or 우범위를 이진탐색하는 것이다.
'''