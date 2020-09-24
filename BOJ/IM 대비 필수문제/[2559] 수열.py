N, K = map(int, input().split())
tem = list(map(int, input().split()))
maxi = bef = sum(tem[:K])
# 현재 합 - 가장 첫 원소 + 마지막 원소 다음 원소 = 다음 합
for i in range(1, N-K+1):
    bef += (tem[i+K-1]-tem[i-1])
    if bef > maxi :
        maxi = bef
print(maxi)


# 2559 시간 초과
# N, K = map(int, input().split())
# temp = list(map(int, input().split()))
# maxi = sum(temp[:K])
# for i in range(1, N-K):
#     temp_sum = sum(temp[i:i+K])
#     if temp_sum > maxi :
#         maxi = temp_sum
# print(maxi)