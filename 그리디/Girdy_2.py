'''
입력받은 문자열을 숫자 단위로 분리
0과 1은 더하고, 나머지 숫자는 곱한다
리스트에서 하니씩 꺼내서 연산하는것으로
'''

'''
곱하는 수와 곱해지는 수 둘 중에 하나라도 1이거나 0이면 더하는게 낫다
이 점을 간과함 !!!!!!!!! Check Point
'''

array = list(map(int,input()))
result = 0

for num in array:
    # num == 1 or num == 0 or result == 0 or result == 1은 너무 비효율적인 코드
    if num <= 1  or result <= 1:
        result += num
    else:
        result *= num
print(result)