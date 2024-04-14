N = int(input())

arr = []
for i in range(N):
    A, B = map(int, input().split())
    arr.append([A, B])
arr = sorted(arr, key = lambda point: (point[1], point[0]))

for i in range(N):
    print(*arr[i])