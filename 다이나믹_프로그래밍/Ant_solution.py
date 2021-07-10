# 다이나믹 프로그래밍(Dynamic Programing - BottomUp)

n =int(input())
food = list(map(int,input().split()))

# 계산된 결과들을 저장하기 위한 테이블
dp_table = [0]*n

# 피보나치 수열에서 처럼 초기값을 설정해야 하는 부분이 있다.
## 초기값을 가지는 dp table이 있기 때문에 반복문을 통해
### 자동계산이 수행된다.
dp_table[0] = food[0]
dp_table[1] = max(food[0],food[1])

'''
i번째 약탈을 할지 안할지는 i-1번째 까지의 최댓값과 비교해서 결정한다.
따라서 직접 비교대상은 i-1인데 이때 i-2까지의 최댓값과 i를 더하는 것을
새로운 최댓값 후보가 되므로 dp[i-1]과dp[i-2]+i 중 max 값을 dp[i]에
저장한다.
'''
for i in range(2,n):
    dp_table[i] = max(dp_table[i-1],dp_table[i-2]+food[i])

print(dp_table[n-1])