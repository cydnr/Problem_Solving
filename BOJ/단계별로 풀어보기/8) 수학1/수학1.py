# 1712 손익분기점
A, B, C = map(int, input().split())
if C-B <= 0:
    result = -2
else:
    result = A//(C-B)
print(result+1)

# 2839 설탕 배달
N = int(input())
five = N//5
flag = False
while five >=0:
    remain = N - five*5
    if remain % 3 == 0:
        three = remain //3
        flag = True
        break
    five -= 1
if flag:
    print(five+three)
else:
    print(-1)

# 2292 벌집