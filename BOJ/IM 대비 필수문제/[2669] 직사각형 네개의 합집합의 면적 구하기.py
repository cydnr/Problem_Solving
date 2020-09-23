# 각 사각형의 왼쪽 아래 점을 point에 겹치지 않게 저장해서 개수 반환.
point = []
for t in range(4):
    square = list(map(int, input().split()))
    for x in range(square[0], square[2]):
        for y in range(square[1], square[3]):
            if (x,y) not in point :
                point.append((x,y))
print(len(point))