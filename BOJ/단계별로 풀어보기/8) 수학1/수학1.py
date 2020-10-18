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
N = int(input())
room = 1
layer= 1
while room < N:
    room += 6*layer
    layer += 1
print(layer)

# 1139 분수찾기
N = int(input())
till = 0
cnt = 1
while till < N :
    till += cnt
    cnt += 1
gap = till-N
if cnt % 2 :
    print('{}/{}' .format(cnt-gap-1, 1+gap))
else :
    print('{}/{}' .format(1+gap, cnt-gap-1))

# 2869 달팽이는 올라가고 싶다
A, B, V = map(int, input().split())
print( (V-A)//(A-B) +2 if (V-A)%(A-B) else (V-A)//(A-B) +1)

