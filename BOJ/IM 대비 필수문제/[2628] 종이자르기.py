# 높이, 너비 각각 배열을 만들어서, 자르는 점들을 넣기
w, h = map(int, input().split())
cut = int(input())
width = [0, w]
height = [0, h]
for i in range(cut):
    dir, n = map(int, input().split())
    if dir == 0:
        height.append(n)
    else:
        width.append(n)

# 순서대로 정렬
width.sort()
height.sort()

# 가장 넓은 구역은 가장 긴 높이 * 가장 긴 너비
max_width = 0
for i in range(len(width)-1):
    wid = width[i+1] - width[i]
    if wid > max_width:
        max_width = wid

max_height = 0
for i in range(len(height)-1):
    hei = height[i+1] - height[i]
    if hei > max_height:
        max_height = hei

print(max_height*max_width)
