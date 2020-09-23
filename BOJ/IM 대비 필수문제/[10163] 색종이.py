N = int(input())
mat = [[0]*101 for _ in range(101)]

# 각 색종이 순서대로 해당 위치에 n을 저장
for n in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for i in range(w):
        for j in range(h):
            mat[x+i][y+j] = n

# many의 n번째 idx에는 mat에서 n인 칸이 몇개인지 저장
many = [0]*(N+1)
for i in range(101):
    for j in range(101):
        for k in range(N+1):
            if mat[i][j] == k:
                many[k] += 1
for i in range(1, N+1):
    print(many[i])