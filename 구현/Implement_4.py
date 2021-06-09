str_ = list(input())
count = 0
new_str = []

for i in str_:
    if i.isalpha() == False:
        count += int(i)
    else:
        new_str.append(i)

new_str.sort()
if count != 0:
    new_str.append(str(count)  )

print("".join(new_str))