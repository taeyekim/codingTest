T = int(input())

arr = [0] * 5 # AXIS, Q1, Q2, Q3, Q4

for tc in range(1, T+1):
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        arr[0] += 1
    elif x > 0 and y > 0:
        arr[1] += 1
    elif x < 0 and y > 0:
        arr[2] += 1
    elif x < 0 and y < 0:
        arr[3] += 1
    elif x > 0 and y < 0:
        arr[4] += 1
    
print(f"Q1: {arr[1]}")
print(f"Q2: {arr[2]}")
print(f"Q3: {arr[3]}")
print(f"Q4: {arr[4]}")
print(f"AXIS: {arr[0]}")