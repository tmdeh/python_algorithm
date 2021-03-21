N, M, K = map(int, input().split());
#N: 배열크기 M: 더해야할 횟수 K: 한개의 수를 최대 반복해서 더할 수 있는 수

array = list(map(int, input().split()))
#N개의 수를 공백으로 구분하여 받기

array.sort() #입력받은 수들 정렬하기

res = 0
first = array[N - 1]
second = array[N - 2]
while True:
    for i in range (K): #가장 큰 값들 K번 더하기
        if M == 0: #M이 0이라면 탈출
            break
        res += first
        M -= 1 #더할 때마다 1씩 빼기
    if M == 0:
        break
    res += second
    M -= 1

print(res)