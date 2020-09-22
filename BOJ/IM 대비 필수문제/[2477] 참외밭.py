N = int(input())
peri = []
for i in range(6):
    peri.append(list(map(int, input().split())))
w = h = 0

# 너비, 높이와 그 idx 찾기
for i in range(6):
    if peri[i][0] in [1,2]:
        if peri[i][1] > w :
            w = peri[i][1]
            w_idx = i
    if peri[i][0] in [3,4]:
        if peri[i][1] > h :
            h = peri[i][1]
            h_idx = i

# 만약 h -> w 순이라면 w에서 두/세 칸 떨어진, 
if w_idx == (h_idx+1)%6:
    a, b = peri[(w_idx+2)%6][1], peri[(w_idx+3)%6][1]
# 만약 w -> h 순이라면 h에서 두/세 칸 떨어진, 
else:
    a, b = peri[(h_idx+2)%6][1], peri[(h_idx+3)%6][1]

print(N*(w*h-a*b))