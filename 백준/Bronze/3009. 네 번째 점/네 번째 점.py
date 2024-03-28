arr = []
arr.append(list(map(int, input().split())))
arr.append(list(map(int, input().split())))
arr.append(list(map(int, input().split())))

x = []
x.append(arr[0][0])
x.append(arr[1][0])
x.append(arr[2][0])

y = []
y.append(arr[0][1])
y.append(arr[1][1])
y.append(arr[2][1])

for i in set(x):
    if x.count(i) == 1:
        ans_x = i

for i in set(y):
    if y.count(i) == 1:
        ans_y = i
print(ans_x, ans_y)
