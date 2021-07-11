n = int(input())

count = 0

def Cal(n):
    if n % 5 == 0:
        n = n // 5
    elif n % 3 == 0:
        n = n // 3
    elif n % 2 == 0:
        n = n // 2
    else:
        n -= 1
    return n


while n != 1:
    if n == 2:
        count+=1
        break
    elif Cal(n-1) < Cal(n):
        n = Cal(n-1)
        count += 2
    elif Cal(n-1) >= Cal(n):
        n = Cal(n)
        count += 1

print(count)