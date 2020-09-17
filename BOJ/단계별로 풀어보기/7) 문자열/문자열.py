# 11654 아스키 코드
C = input()
print(ord(C))

# 11720 숫자의 합
N = int(input())
li = input()
result = 0
for i in range(N):
    result += int(li[i])
print(result)

#10809 알파벳 찾기
word = input()
alpha = [-1]*26
for i in range(26):
    alpha[i] = word.find(chr(97+i))
for i in range(26):
    print(alpha[i], end=" ")

# 2675 문자열 반복
T = int(input())
for t in range(T):
    N, word = map(str, input().split())
    N = int(N)
    P =''
    for i in range(len(word)):
        P += word[i]*N
    print(P)

# 1157 단어 공부
word = list(input())
alphas = {}
for i in range(len(word)):
    if 97 <= ord(word[i]) <= 122:
        word[i] = chr(ord(word[i])-32)
    if word[i] not in alphas:
        alphas[word[i]] = 1
    else :
        alphas[word[i]] += 1
maxch = ''
maxnum = max(alphas.values())
for ch, num in alphas.items():
    if num == maxnum:
        if not maxch:
            maxch = ch
        else:
            maxch = '?'
            break
print(maxch)

# 1152 단어의 개수
sen = list(input().split())
print(len(sen))

# 2908 상수
A, B = map(list, input().split())
a = ''
b = ''
for i in range(2,-1,-1):
    a += A[i]
    b += B[i]
a, b = int(a), int(b)
if a > b:
    print(a)
else:
    print(b)

# 5622 다이얼
dial = list(input())
time = 0
for d in range(len(dial)):
    num = ord(dial[d])-65
    if num >= 25:
        num -=2
    elif num >=18 :
        num -=1
    time += (num//3)+3
print(time)

# 2941 크로아티아 알파벳
cro = input()
alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(len(alpha)) :
    cro = cro.replace(alpha[i], '1')
print(len(cro))

'''
# 실패한 코드
cro = list(input())
cnt = 0
idx = 0
while idx < len(cro):
    if cro[idx] in ['c', 'd', 's', 'z'] :
        if idx + 1 < len(cro) :
            if cro[idx+1] in ["=", '-']:
                idx += 1
            elif cro[idx+1]=='z':
                if idx+2 <len(cro) and cro[idx+2]=='=' :
                    idx += 2
    elif cro[idx] in ['l', 'n'] :
        if idx + 1 < len(cro) :
            if cro[idx+1] == 'j':
                idx += 1
    cnt += 1
    idx += 1
print(cnt)
'''

# 1316 그룹 단어 체커
def isgroup(word):
    chars = [word[0]]
    top = 0
    flag = 1
    for i in range(1,len(word)) :
        if word[i] != chars[top] :
            if word[i] not in chars :
                chars.append(word[i])
                top +=1
            else :
                flag = 0
                break
    return flag

T = int(input())
result = 0
for t in range(T):
    a = isgroup(input())
    result += a
print(result)
        