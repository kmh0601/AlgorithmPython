str = list(input())
count = 0
new_str = []

for i in str:
    if i.isalpha() == False:
        count += int(i)
    else:
        new_str.append(i)

new_str.sort()
new_str.append(count)

for i in new_str:
     print(i, end ='')