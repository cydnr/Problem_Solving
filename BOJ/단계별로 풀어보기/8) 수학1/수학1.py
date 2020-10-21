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

# 10250 ACM호텔
T = int(input())
for t in range(T):
    H, W, N = map(int, input().split())
    ho = (N // H) + 1
    floor = N % H
    if not floor:
        floor = H
        ho -= 1
    result = str(floor)
    if ho<10:
        result += '0'+str(ho)
    else:
        result += str(ho)
    print(result)

# 2775 부녀회장이 될테야
arr = [[1] for _ in range(15)]
arr[0] = list(range(1,16))
for i in range(1,15):
    for j in range(1,15):
        arr[i].append(arr[i][j-1]+arr[i-1][j])
T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n-1])