# 10818 최소, 최대
N = int(input())
li = list(map(int, input().split()))
print(min(li), max(li))

# 2562 최댓값
maxi = int(input())
maxidx = 0
for i in range(1, 9):
    cur = int(input())
    if cur > maxi:
        maxi = cur
        maxidx = i
print(maxi)
print(maxidx+1)

# 2577 숫자의 개수
A = int(input())
B = int(input())
C = int(input())
li = list(str(A*B*C))
for i in range(0, 10):
    print(li.count(str(i)))

# 3052 나머지
remainder = set()
for i in range(10):
    remainder.add(int(input())%42)
print(len(remainder))


# 1546 평균
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
for i in range(N):
    scores[i] = scores[i]/M*100
print(sum(scores)/N)

# 8958 OX퀴즈
N = int(input())
for i in range(N):
    correct = list(input())
    if correct[0] == 'O':
        score = 1
    else :
        score = 0
    total = score
    for i in range(1,len(correct)):
        if correct[i] == 'O':
            if score != 0 :
                score += 1
            else :
                score = 1
            total += score
        else :
            score = 0
    print(total)

'''
# Runtime error
N = int(input())
for i in range(N):
    correct = list(input())
    if correct[i] == 'O':
        scores = [1]
    else:
        scores = [0]
    for i in range(1, len(correct)):
        if correct[i] == 'O':
            if scores[i-1] == 0:
                scores.append(1)
            else:
                scores.append(scores[i-1]+1)
        else :
            scores.append(0)
    print(sum(scores))
'''