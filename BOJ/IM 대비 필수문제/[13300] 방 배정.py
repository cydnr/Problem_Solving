N, K = map(int, input().split())
# 학년별로 성별이 있는 2차원 배열에, 학생 추가
people = [[0,0] for _ in range(6)]
for n in range(N):
    S, Y = map(int, input().split())
    people[Y-1][S] += 1

# 각 학년+성별로 방의 개수 구해서 총 개수 구하기 
room = 0
for grade in range(6):
    for gender in range(2):
        x = people[grade][gender]
        if x > 0:
            room += (1 + (x-1)//K)
print(room)