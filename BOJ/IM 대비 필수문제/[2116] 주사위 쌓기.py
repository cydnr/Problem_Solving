# 반대편 idx 구해주는 함수
def opposite(k):
    if k == 0 : return 5
    elif k == 1: return 3
    elif k == 2: return 4
    elif k == 3: return 1
    elif k == 4: return 2
    elif k == 5: return 0

# a번째 주사위의 바닥이 b일때, (옆면 중 가장 큰 값, 윗면) 반환
def find_large(a, b):
    b_idx = dices[a].index(b)
    t_idx = opposite(b_idx)
    t = dices[a][t_idx]
    l = 1
    for i in range(1, 7):
        if i not in (t, b):
            l = i
    return l, t

N = int(input())
dices = []
for n in range(N):
    dice = list(map(int, input().split()))
    dices.append(dice)

# 첫번째 주사위의 밑면을 1~6까지 다 해본다
big = 0                                     # 숫자 합이 가장 큰 경우
for i in range(1,7) :
    bottom = i                              # 첫 주사위 밑면이 i일 때
    adding = 0                              # 옆면의 합을 최대화해서 저장
    for nth in range(N):                    # n번째 주사위에 대하여
        ans, top = find_large(nth, bottom)  # 몇번쨰 주사위의 바닥인지를 넘기면, (옆면 중 가장 큰 값, 윗면) 반환
        adding += ans
        bottom = top
    if adding > big:
        big = adding
print(big)        










