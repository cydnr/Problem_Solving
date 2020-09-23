# 성별과 규칙에 맞춰 껐다 켜기
# 인덱스와 스위치 번호를 맞추기 위해 list 처음에 0 추가. 
N = int(input())
light = [0] + list(map(int, input().split()))
student = int(input())
for s in range(student):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(0, N+1, num):
            light[i] = (light[i]+1)%2
    else:
        left = right = num
        while True :
            if 1<=left and right<=N:
                if light[left] == light[right]:
                    light[left] = light[right] = (light[left]+1)%2
                    left -= 1
                    right += 1
                else: break
            else: break
# 20개 찍을 때마다 줄바꿈.
for i in range(1, N+1):
    print(light[i], end=' ')
    if i % 20 == 0:
        print()