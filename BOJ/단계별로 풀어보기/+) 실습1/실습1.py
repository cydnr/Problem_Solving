# 10039 평균 점수
scores = []
for i in range(5) :
    score = int(input())
    if score < 40 :
        score = 40
    scores.append(score)
print(sum(scores)//5)

# 5543 상근날드
minburger = minbev = 2001
for i in range(3) :
    burger = int(input())
    if burger < minburger :
        minburger = burger
for i in range(2) :
    beverage = int(input())
    if beverage < minbev :
        minbev = beverage
print(minbev+minburger-50)

# 10817 세 수
A, B, C = map(int, input().split())
li = [A, B, C]
li.sort()
print(li[1])

# 2523 별 찍기 - 13
N = int(input())
for i in range(1, N) :
    print('*'*i)
for i in range(N, 0, -1):
    print('*'*i)

# 2446 별 찍기 - 9
N = int(input())
for i in range(0, N):
    print(' '*i, end='')
    print('*'*((N-i)*2-1))
for i in range(2, N+1):
    print(' '*(N-i), end='')
    print('*'*(2*i-1))

# 10996 별 찍기 - 21
N = int(input())
for i in range(2*N):
    if i % 2:
        for j in range(N):
            if j % 2:
                print('*', end='')
            else :
                print(' ', end='')
    else:
        for j in range(N):
            if j % 2 :
                print(' ', end='')
            else :
                print('*', end='')
    print()
