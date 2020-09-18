# 입력 받기
N = int(input())
nums = list(map(int, input().split()))

# 1번 넣고 시작
ord = [1]

# 2번에서 마지막 번호까지, 위치에 맞게 insert
for i in range(1,N):
    card = nums[i]
    ord.insert(i-card, i+1)

# 출력
for i in ord :
    print(i, end=" ")