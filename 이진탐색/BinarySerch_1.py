def BinarySerch(list, target, start, end):
    if start > end:
        print("{}을(를) 찾을 수 없습니다.".format(target))
        return
    mid = (start+end) // 2

    if list[mid] > target:
        BinarySerch(list, target, start, mid-1)
    elif list[mid] < target:
        BinarySerch(list, target, mid+1, end)
    # list[mid] == target
    else:
        print("찾았습니다. {}은(는) {}번째에 있습니다." .format(target, mid+1))

def IterativeBinarySerch(list, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if list[mid] < target:
            start = mid + 1
        elif list[mid] > target:
            end = mid - 1
        else:
            print("찾았습니다. {}은(는) {}번째에 있습니다." .format(target, mid+1))
            return
    print("{}을(를) 찾을 수 없습니다.".format(target))


Num = [1,3,5,8,12,23,34]

BinarySerch(Num,8,0,len(Num)-1)
BinarySerch(Num,9,0,len(Num)-1)
BinarySerch(Num,34,0,len(Num)-1)
IterativeBinarySerch(Num, 1, 0, len(Num)-1)
IterativeBinarySerch(Num, 2, 0, len(Num)-1)
IterativeBinarySerch(Num, 3, 0, len(Num)-1)