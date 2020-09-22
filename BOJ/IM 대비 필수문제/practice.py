for t in range(4) :
    sq = list(map(int, input().split()))
    if (sq[0], sq[1]) == (sq[6], sq[7]) or (sq[2], sq[3]) == (sq[4], sq[5]):
        ans = 'c'
    