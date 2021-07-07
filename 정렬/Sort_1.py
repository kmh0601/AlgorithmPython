n, k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def QuickSort(list,start,end):
    if start >= end:
        return

    pivot = start
    left = pivot+1
    right = end

    while left < right:
        for i in range(left,end+1):
            left = i
            if list[pivot] < list[left]:
                break
        for i in range(end,pivot-1,-1):
            right = i
            if list[pivot] > list[right]:
                break
        if left >= right:
            list[pivot], list[right] = list[right], list[pivot]
        else:
            list[left], list[right] = list[right], list[left]
    QuickSort(list,start,right-1)
    QuickSort(list,right+1,end)

#QuickSort(A,0,len(A)-1)
#QuickSort(B,0,len(B)-1)
#B = B[::-1]
A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i] = B[i]
    else:
        break

print(sum(A))

