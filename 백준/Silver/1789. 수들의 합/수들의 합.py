N = int(input())
total = 0
i = 0
while True:
    i += 1
    total += i
    if total > N:
        break
    
print(i-1)
