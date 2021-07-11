n, m = map(int,input().split())
money = []

####TIP)애초에 dp에 default 값을 조건을 뛰어넘는 큰 숫자로 두면 min을 실행할 때, 자동으로 불가능한 경우는 선택이 되지 않도록 할 수 있다!!!!
##default값을 설정하기에 번거로운 경우에 자주 이용하자.
dp = [10001] * (m+1)
dp[0] = 0

for i in range(n):
    money.append(int(input()))

# 값을 구하지 않은 dp테이블을 채워넣는다. == index 1 ~ index m+1
for i in range(1,m+1):
        '''
        # 일단 default 값으로 가능한 아무값이나 설정해준다
        for coin in money:
            if i-coin >= 0 and dp[i-coin] != -1:
                dp[i] = dp[i-coin]+1
                break
            # default 값 설정이 불가능한 경우
            else:
                dp[i] = -1
        #dp[i] == -1이면 이미 만들 수 있는 경우의 수가 없으므로(그리고 어차피 min을 진행하면 -1이 선택될 수 밖에 없음)
        if dp[i] != i:
        '''
        # 화폐단위를 하나씩 꺼낸다
        for coin in money:
            #화폐단위를 뺀 금액을 만들 경우의 수가 존재한다면 dp[i]의 값으로 설정한다. 이때, 최솟값이므로 모든 화폐단위에 대해 비교해서 min값을 넣는다.
            dp[i] = min(dp[i], dp[i-coin]+1)
if dp[m] != 10001:
    print(dp[m])
else:
    print(-1)
print(dp)