N, K = input().split()
N = int(N)
K = int(K)
# N, K = map(int, input().split()) map함수를 통한 코드 절약
cnt = 0

while N != 1:
    if(N%K != 0):
        N -= 1
    else:
        N //=K
    cnt += 1
print(cnt)
