'''
for t in range(4) :
    sq = list(map(int, input().split()))
    if (sq[0], sq[1]) == (sq[6], sq[7]) or (sq[2], sq[3]) == (sq[4], sq[5]):
        ans = 'c'
'''


        
def who_win():
    if A[1:].count(4) > B[1:].count(4):
        return 'A'
    elif A[1:].count(4) < B[1:].count(4):
        return 'B'
    else:
        if A[1:].count(3) > B[1:].count(3):
            return 'A'
        elif A[1:].count(3) < B[1:].count(3):
            return 'B'
        else:
            if A[1:].count(2) > B[1:].count(2):
                return 'A'
            elif A[1:].count(2) < B[1:].count(2):
                return 'B'
            else:
                if A[1:].count(1) > B[1:].count(1):
                    return 'A'
                elif A[1:].count(1) < B[1:].count(1):
                    return 'B'
                else:
                    return 'D'

N = int(input())
for n in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = who_win()
    print(result)