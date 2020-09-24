cheolsu = []
for i in range(5):
    cheolsu.append(list(map(int, input().split())))

moderator = []
for i in range(5):
    moderator.extend(list(map(int, input().split())))

cnt = 0
while cnt<25:
    x = moderator[cnt]
    flag = False
    # 부르는 숫자는 0으로 바꿈
    for i in range(5):
        for j in range(5):
            if cheolsu[i][j] == x:
                cheolsu[i][j] = 0
                flag = True
                break
        if flag : break
    # 적어도 12개는 있어야 3빙고 가능, 빙고 개수 세기
    if cnt >= 11 :
        bingo = 0
        d1 = d2 = True
        for i in range(5):
            if cheolsu[i][i] !=0:
                d1 = False
            if cheolsu[i][4-i] !=0:
                d2 = False
            row = col = True
            for j in range(5):
                if cheolsu[i][j] != 0:
                    row = False
                if cheolsu[j][i] != 0:
                    col = False
            if row : bingo += 1
            if col : bingo += 1 
        if d1 : bingo += 1
        if d2 : bingo += 1
        if bingo >=3 :
            break
    cnt += 1
print(cnt+1)