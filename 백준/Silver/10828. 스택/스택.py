import sys

# 입력 함수를 빠른 sys.stdin.readline으로 변경
input = sys.stdin.readline

stack = []

N = int(input())

for _ in range(N):
    lst = list(input().split())
    order = lst[0]
    if order == "push":
        stack.append(lst[1])
    elif order == "pop":
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) >= 1:
            print(stack[-1])
        else:
            print(-1)