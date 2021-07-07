from bisect import bisect_left, bisect_right

def CountByRange(list, start, end):
    left = bisect_left(list,start)
    right = bisect_right(list,end)
    return (right - left)

Num = [1,1,2,3,4,5,5,5,6,7,8,9]
print("x =",Num)
print("4 <= x <= 4 인 x는 총 {}개 있습니다.".format(CountByRange(Num,4,4)))
print("1 <= x <= 5 인 x는 총 {}개가 있습니다.".format(CountByRange(Num,1,5)))