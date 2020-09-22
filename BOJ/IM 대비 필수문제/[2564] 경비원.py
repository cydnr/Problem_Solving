# 왼쪽 위를 시작점으로 생각, 시계방향으로 돌면서 시작점에서 얼마나 떨어져있는지 계산
def cal_position(dir, pos):
    if dir == 1:
        return pos
    elif dir == 2:
        return  w + h + (w-pos)
    elif dir == 3:
        return 2 * (w+h) - pos
    else:
        return w + pos


w, h = map(int, input().split())
N = int(input())
stores =[]
for n in range(N):
    store = list(map(int, input().split()))
    stores.append(store)
d_dir, d_pos = map(int, input().split())

d = cal_position(d_dir,d_pos)
perimeter = 2 * (w+h)
ans = 0

# 각 가게의 위치를 받아, 동근과의 거리 계산.
for i in range(len(stores)):
    s_dir, s_pos = stores[i][0], stores[i][1]
    s = cal_position(s_dir,s_pos)
    if d > s :
        x = d-s
    else:
        x =  s-d
    # 더 빨리 도달하는 쪽
    diff = min(x, perimeter - x)
    ans += diff
print(ans)