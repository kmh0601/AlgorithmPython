N = int(input())

time = list(range(0,60))

i = 0
count = 0

while i <= N:
    if i % 10 == 3:
        count += 3600
        i += 1
    else:
        for min in time:
            if min % 10 == 3 or min // 10 == 3:
                count += 60
            else:
                for sec in time:
                    if sec % 10 == 3 or sec // 10 == 3:
                        count += 1
        i += 1
print(count)