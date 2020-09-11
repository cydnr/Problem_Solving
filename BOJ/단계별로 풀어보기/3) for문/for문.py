# 2739 구구단
N = int(input())
for i in range(1, 10):
    print('{} * {} = {}' .format(N, i, N*i))

# 10950 A+B - 3
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print(A + B)

# 8339 합
N = int(input())
print((N*(N+1))//2)

# 15552 빠른 A+B **
import sys
N = int(input())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)

# 2741 N 찍기
N = int(input())
for i in range(1, N + 1):
    print(i)

# 2742 기찍N
N = int(input())
for i in range(N, 0, -1):
    print(i)

# 11021 A+B - 7
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print('Case #{}: {}' .format(i + 1, A + B))

# 11022 A+B - 8
N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}' .format(i + 1, A, B, A + B))

# 2438 별 찍기 - 1
N = int(input())
for i in range(1,N+1):
    print('*'*i)

# 2439 별 찍기 - 2
N = int(input())
for i in range(1,N+1):
    print(' '*(N-i), end='')
    print('*'*i)

# 10871 X보다 작은 수
N, X =  map(int, input().split())
A = list( map(int, input().split()))
for a in A:
    if a < X:
        print(a, end=' ')