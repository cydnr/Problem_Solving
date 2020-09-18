
'''
cheolsu = [[11, 12, 2, 24, 10], [16, 1, 13, 3, 25], [6, 20, 5, 21, 17], [19, 4, 8, 14, 9], [22, 15, 7, 23, 18]]
moderator = [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]
'''

def bingo():
    b = 0
    diag1 = diag2 = True
    for i in range(5):
        row = col = True
        for j in range(5):
            if cheolsu[i][j]:
                row = False
            if cheolsu[j][i]:
                col = False
            if i == j :
                if cheolsu[i][j]:
                    diag1 = False
            if i == 4-j :
                if cheolsu[i][j]:
                    diag2 = False
        if row : b += 1
        if col : b += 1
    if diag1 : b += 1
    if diag2 : b += 1
    if b >= 3 : return True
    else : return False

cheolsu = []
for i in range(5):
    cheolsu.append(list(map(int, input().split())))

moderator = []
for i in range(5):
    moderator.extend(list(map(int, input().split())))

for i in range(5):
    for j in range (5):
        if cheolsu[i][j] in moderator[:11] :
            cheolsu[i][j] = 0

idx =12
while True :
    flag = False
    for i in range(5):
        for j in range(5):
            if cheolsu[i][j] == moderator[idx] :
                cheolsu[i][j] = 0
                flag = True    
                break
        if flag :
            break
    result = bingo()
    if result : break
    idx += 1

print(idx+1)