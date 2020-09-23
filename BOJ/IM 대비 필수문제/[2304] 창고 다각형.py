N = int(input())
poles = []
highest = 0
for n in range(N):
    L, H = map(int, input().split())
    if highest < H:
        highest = H
        h_idx = L
    poles.append([L, H])

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

area = highest
for i in range(0,len(left)-1):
    if left[i][1] > left[i+1][1]:
        left[i+1][1] = left[i][1]
    area += left[i][1] * (left[i+1][0] - left[i][0])
print(area)

# 오른쪽 넓이 구하기