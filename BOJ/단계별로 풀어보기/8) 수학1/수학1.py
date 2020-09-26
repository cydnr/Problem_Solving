# 1712 손익분기점
A, B, C = map(int, input().split())
if C-B <= 0:
    result = -2
else:
    result = A//(C-B)
print(result+1)