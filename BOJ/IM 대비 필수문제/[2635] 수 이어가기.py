# N//2 부터 N까지 수를 brute force로 연산.
N = int(input())
max_cnt = 2
for i in range(N//2, N+1):
    a, b = N, i
    cnt = 2
    while a - b >= 0 :
        a, b = b, a - b
        cnt +=1
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = i

print(max_cnt)
a, b = N, max_num
print('{} {}'.format(a, b), end=' ')
while a - b > 0:
    print(a-b, end=' ')
    a, b = b, a - b