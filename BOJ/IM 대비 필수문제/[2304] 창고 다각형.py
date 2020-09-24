N = int(input())
poles = []
highest = 0

# 기둥 위치, 높이 저장하며 가장 높은 것 찾기
for n in range(N):
    L, H = map(int, input().split())
    if highest < H:
        highest = H
        h_idx = L
    poles.append([L, H])

# 가장 높은 것 기준으로 왼편, 오른편 나누기
left = []
right = []
for i in range(N):
    if poles[i][0] <= h_idx :
        left.append(poles[i])
    elif poles[i][0] > h_idx :
        right.append(poles[i])
right.append([h_idx, highest])
left.sort()
right.sort()

# 가장 높은 것 area에 넣고 시작
area = highest

# area에 기둥 왼편 다각형 넓이 더하기
for i in range(0,len(left)-1):
    if left[i][1] > left[i+1][1]:
        left[i+1][1] = left[i][1]
    area += left[i][1] * (left[i+1][0] - left[i][0])

# area에 기둥 오른편 다각형 넓이 더하기
for i in range(len(right)-1, 0, -1):
    if right[i][1] > right[i-1][1]:
        right[i-1][1] = right[i][1]
    area += right[i][1]* (right[i][0] - right[i-1][0])

print(area)