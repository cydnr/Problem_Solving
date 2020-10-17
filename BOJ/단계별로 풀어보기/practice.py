'''
N = int(input())
layer = (N-1)//6
result = 0
rooms = 1
while result<layer:
    rooms += 1
    result += rooms
print(rooms)
'''