N = int(input())
paper = [[0]*100 for _ in range(100)]
cnt = 0
for n in range(N):
    x, y = map(int, input().split())
    for a in range (x, x+10):
        for b in range (y, y +10):
            # 색종이가 아직 덮혀있지 않으면, 덮고 +1
            if not paper[a][b] :
                paper[a][b] = 1
                cnt += 1
print(cnt)