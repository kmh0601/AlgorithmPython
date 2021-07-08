# CountByRange와 같은 기능

n, m = map(int,input().split())
num = list(map(int,input().split()))

def LeftBinarySearch(list,target,start,end):
    while start <= end:
        mid = (start+end) // 2
        # list[mid] == target 일때 왼쪽 부분을 탐색하게 한다면 결국에 target의 왼쪽 끝점에 도달한다.
        if list[mid] >= target:
            end = mid - 1
        elif list[mid] < target:
            start = mid + 1

    # 마지막에 결국 end = mid - 1이 되므로 start값이 변하지 않는 값, 즉 우리가 원하는 값이다
    return start


def RightBinarySearch(list, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if list[mid] > target:
            end = mid - 1
            # list[mid] == target 일때 오른쪽 부분을 탐색하게 한다면 결국에 target의 오른쪽 끝점에 도달한다.
        elif list[mid] <= target:
            start = mid + 1

    # 마지막에 결국 start = mid + 1이 되므로 end값이 변하지 않는 값, 즉 우리가 원하는 값이다
    return end

result = (RightBinarySearch(num, m, 0, n-1) - LeftBinarySearch(num, m, 0, n-1))
if result != 0:
    print(result+1)
else:
    print(-1)