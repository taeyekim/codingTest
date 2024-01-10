N = int(input())
se = set(map(int,input().split()))
M = int(input())
li = list(map(int,input().split()))

for i in li:
    if i in se:
        print(1)
    else:
        print(0)