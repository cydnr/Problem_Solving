# 10158 시간 초과
# 개미가 오가는 범주는 2*w, 2*h임을 이용.
# 아이디어 힌트 : https://beyond1.tistory.com/60
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p = (p+t) % (2*w)
q = (q+t) % (2*h)
if p > w : p = 2*w - p
if p > h : q = 2*h - q
print(p, q)
# 시간 초과 해결할 방법을 찾지 못해서 그냥 C언어로 구현해서 제출

# 10158 메모리 에러
# def findpos(w, h, p, q, t):
#     dir1 = dir2 = 1
#     cnt = -1
#     startx, starty = p, q
#     pattern = []
#     while cnt <=t :
#         pattern.append([p,q])
#         if p+dir1 > w or p+dir1 < 0 :
#             dir1 = -dir1
#         elif q+dir2 > h or q+dir2 < 0 :
#             dir2 = -dir2
#         p += dir1
#         q += dir2
#         if p == startx and q == starty :
#             break
#         cnt += 1
#     if t+1 == len(pattern):
#         return pattern[t]
#     else :
#         idx = t % (len(pattern))
#         return pattern[idx]


# W, H = map(int, input().split())
# P, Q = map(int, input().split())
# T = int(input())
# ans = findpos(W, H, P, Q, T)
# print(ans[0], ans[1])
