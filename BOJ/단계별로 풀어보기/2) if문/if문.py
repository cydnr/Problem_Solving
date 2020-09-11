# 1330 두 수 비교하기
A, B = map(int, input().split())
if A > B:
    print('>')
elif A == B:
    print('==')
else:
    print('<')

# 9498 시험 성적
S = int(input())
if S >= 90:
    print('A')
elif S >= 80:
    print('B')
elif S >= 70:
    print('C')
elif S >= 60:
    print('D')
else:
    print('F')

# 2753 윤년
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(1)
        else :
            print(0)
    else :
        print(1)
else :
    print(0)

# 14681 사분면 고르기
x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)

# 2884 알람 시계
H, M = map(int, input().split())
if M >= 45:
    M = M - 45
else:
    M = 60 - (45 - M)
    if H > 0:
        H -= 1
    else:
        H = 23
print('{} {}' .format(H, M))