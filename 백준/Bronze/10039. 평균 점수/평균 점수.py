arr = []
for i in range(5):
    arr.append(int(input()))
    
total = 0
for i in range(5):
    if arr[i] <= 40:
        total += 40
    else:
        total += arr[i]
print(total // 5)