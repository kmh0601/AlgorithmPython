Num = [3,8,19,3,12,8,4,32,10,5,12]

def QuickSort(list, start, end):
    pivot = start
    left = pivot + 1
    right = end
    # start == end 즉, 정렬할 리스트가 하나일 때까지 호출한다는 뜻
    if start >= end:
        return

    # pivot 기준으로 정렬이 완료되지 않은 상태
    ## right == left 인 경우는 pivot이 최대 혹은 최소 이다
    while right > left:

        # 왼쪽에서부터 pivot 보다 큰 값 찾기
        for i in range(left, end + 1):
            left = i
            if list[pivot] < list[left]:
                break
        # 오른쪽에서부터 pivot 보다 작은 값 찾기
        # pivot -1 까지 찾는 이유는 pivot이 최소값일 수 있기 때문에
        for i in range(right, pivot-1, -1):
            right = i
            if list[pivot] > list[right]:
                break
        # 만약 right <= left 이면 이미 pivot기준 대소관계가 정렬된 것이므로 pivot을 경계에 집어넣음
        if right <= left:
            list[right], list[pivot] = list[pivot], list[right]
        else:
        # right와 left를 교환해준다
            list[right], list[left] = list[left], list[right]
    # sort가 끝났으면 좌우를 다시 QuickSort
    QuickSort(list,start,right-1)
    QuickSort(list,right+1,end)

def SelectionSort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]

def InsertSort(list):
    for i in range(len(list)-1):
        for j in range(i,0,-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
            else:
                break

QuickSort(Num, 0, len(Num) - 1)
#SelectionSort(Num)
#InsertSort(Num)
print(Num[0:])