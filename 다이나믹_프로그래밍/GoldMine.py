# T => 반복 횟수
T = int(input())

# T번 반복한다
for i in range(T):
    # n * m 행렬
    n, m = map(int, input().split())

    # array[] => 주어지는 금광
    temp = list(map(int, input().split()))
    array = []
    for i in range(n):
        array.append(temp[m*i:m*(i+1)])
        '''
        한 줄로 입력되는 것을 이중리스트로 저장하려면 우선 리스트로 만들고 슬라이싱을 통해 이중 리스트로 append 해준다.
        이때, n*m 리스트로 만들려면 슬라이싱을 arr[i*m:(i+1)*m] => i 는 0에서n-1까지 한다.
        이유 : 슬라이싱은 [x:y] 일때 x에서 y-1 까지 즉, y-x개 꺼내기 때문이다.
              따라서 (i+1)*m - i*m = im+m-im= m! m개씩 꺼내는게 된다!
        '''

    # Gold[] => 계산된 금의 양 // max를 통해 구하는 다이나믹 프로그래밍 이므로 각 칸을 0으로 초기화 해줌
    Gold = [[0 for _ in range(m)] for _ in range(n)]


    for j in range(m):
        for i in range(n):
            if j-1 >= 0:
                Gold[i][j] = max(Gold[i][j], Gold[i][j-1]) + array[i][j]
                if i-1 >= 0:
                    Gold[i][j] = max(Gold[i][j], Gold[i-1][j-1]) + array[i][j]
                if i+1 < n:
                    Gold[i][j] = max(Gold[i][j], Gold[i+1][j-1]) + array[i][j]
            else:
                Gold[i][j] = Gold[i][j] + array[i][j]

    result = 0
    for i in range(n):
        result = max(result, Gold[i][m-1])
    print(result)