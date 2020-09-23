# 10157 런타임에러
# def findseat(k):
#     if k > C*R :
#         return 0
#     else :
#         x, y = 1, 1
#         here = 1
#         dir1 = [0, 1, 0, -1, 1, C]
#         dir2 = [1, 0, -1, 0, 1, R]
#         dir = 0
#         while here < k :
#             if dir1[4] <= x+dir1[dir] <= dir1[5] and dir2[4]<= y+dir2[dir] <= dir2[5] :
#                 x += dir1[dir]
#                 y += dir2[dir]
#                 here += 1
#             else : 
#                 if dir == 0:
#                     dir1[4] +=1
#                 elif dir == 1:
#                     dir2[5] -=1
#                 elif dir == 2:
#                     dir1[5] -=1
#                 else :
#                     dir2[4] +=1
#                 dir = (dir+1)%4
#         return [x, y]
                    

# C, R = map(int, input().split())
# K = int(input())
# ans = findseat(K)
# print(ans[0], ans[1])