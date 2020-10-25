# 1987 소수 찾기
N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    num = arr[i]
    if num != 1:
        flag = True
        for k in range(2,num):
            if num % k == 0:
                flag = False
                break
        if flag: cnt += 1
print(cnt)