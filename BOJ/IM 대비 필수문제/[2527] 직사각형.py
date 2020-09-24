for t in range(4) :
    sq = list(map(int, input().split()))
    first_x = set(range(sq[0], sq[2]+1))
    first_y = set(range(sq[1], sq[3]+1))
    second_x = set(range(sq[4], sq[6]+1))
    second_y = set(range(sq[5], sq[7]+1))

    # 두 사각형에서 겹치는 x 좌표, 겹치는 y좌표 각각 저장
    inter_x = first_x&second_x
    inter_y = first_y&second_y

    if len(inter_x) >1 and len(inter_y) >1 :
        ans = 'a'
    elif len(inter_x) == 1 and len(inter_y) == 1:
        ans = 'c'
    elif len(inter_x) ==1 and len(inter_y) >1 :
        ans = 'b'
    elif len(inter_x) > 1 and len(inter_y)  == 1 :
        ans = 'b'
    else:
        ans = 'd'

    print(ans)