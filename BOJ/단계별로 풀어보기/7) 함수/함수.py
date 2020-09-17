# 15596 정수 N개의 합
def solve(a):
    ans = 0
    for item in a :
        ans += item
    return ans

# 4673 셀프 넘버
def generate(k):
    li = str(k)
    for i in li :
        k +=int(i)
    if k <= 10000 :
        self_number[k] = 0
        generate(k)

self_number = [-1]*10001
for i in range(100):
     self_number[i] = 0
for i in [1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97] :
    self_number[i] = 1
    generate(i)

for i in range(100, 10001):
    if self_number[i] == -1 :
        self_number[i] = 1
        generate(i)

for i in range(10001):
    if self_number[i] == 1:
        print(i)

# 1065 한수
def hansu(a):
    if a < 100 :
        return a
    else :
        ans = 99
        for i in range(100, a+1):
            li = list(str(i))
            diff = int(li[0])-int(li[1])
            flag = True
            for j in range(1, len(li)-1):
                if int(li[j])-int(li[j+1]) != diff :
                    flag = False
                    break
            if flag : ans +=1
        return ans

N = int(input())
print(hansu(N))