N = int(input())
nums = list(map(int, input().split()))

# 최장 길이
longest = 1

# 감소하거나 같은 경우
cnt = 1
for i in range(N-1):
    if nums[i] >= nums[i+1]:
        cnt += 1
        if cnt > longest:
            longest = cnt
    else :
        cnt = 1

# 증가하거나 같은 경우
cnt = 1
for i in range(N-1):
    if nums[i] <= nums[i+1]:
        cnt += 1
        if cnt > longest:
            longest = cnt
    else :
        cnt = 1

print(longest)