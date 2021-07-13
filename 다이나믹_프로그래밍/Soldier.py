'''
최장 증가 부분 수열(LIS, Longest Increasing Subsequence)알고리즘
'''
n = int(input())

soldier = list(map(int,input().split()))
soldier.reverse()
dp = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if soldier[j] < soldier[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))