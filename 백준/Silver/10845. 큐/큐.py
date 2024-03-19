import sys

# 입력 함수를 빠른 sys.stdin.readline으로 변경
input = sys.stdin.readline

queue = []

N = int(input())

for _ in range(N):
    lst = list(input().split())
    order = lst[0]
    if order == "push":
        queue.append(lst[1])
    elif order == "pop":
        if len(queue):
            print(queue.pop(0))
        else:
            print(-1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        print(queue[0] if len(queue) else -1)
    else:
        print(queue[-1] if len(queue) else -1)
