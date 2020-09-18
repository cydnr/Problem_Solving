# 입력 받기
heights = []
for i in range(9):
    heights.append(int(input()))

# 제외할 두 난쟁이 찾기
diff = sum(heights)-100
for i in range(8):
    for j in range(i+1,9):
        if heights[i] + heights[j] == diff :
            a, b = heights[i], heights[j]
            break

# 두 난쟁이 제외하기
heights.remove(a)
heights.remove(b)

# 오름차순으로 정렬해 출력
heights.sort()
for h in heights :
    print(h)