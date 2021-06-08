N = int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            # 어떤 숫자가 포함되어 있냐를 알아볼 때는 문자열의 형태로
            # 바꾼 후에 if x in srt 형식을 쓰면 편하다!
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)