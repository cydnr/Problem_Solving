# 10952 A+B - 5
while True:
    A, B = map(int, input().split())
    if A==0: break
    print(A+B)

# 10951 A+B - 4
while True:
    try:
        A, B = map(int, input().split())
        if A==0: break
        print(A+B)
    except :
        break

# 1110 더하기 사이클
N = int(input())
new = (N%10)*10 + ((N//10) + (N%10))%10
cnt = 1
while new != N:
    new = (new%10)*10 + ((new//10) + (new%10))%10
    cnt +=1
print(cnt)

