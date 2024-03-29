n = int(input())
sequence = [int(input()) for _ in range(n)]

ST = []
operations = []
cur = 1

for num in sequence:
    while cur <= num:
        ST.append(cur)
        operations.append('+')
        cur += 1
    if ST[-1] == num:
        ST.pop()
        operations.append('-')
    else:
        print('NO')
        break
else:
    for op in operations:
        print(op)