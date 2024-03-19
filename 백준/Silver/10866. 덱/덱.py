import sys

# 입력 함수를 빠른 sys.stdin.readline으로 변경
input = sys.stdin.readline

dec = []

N = int(input())

for _ in range(N):
    lst = list(input().split())
    order = lst[0]

    if order == "push_back":
        dec.append(lst[1])
    elif order == "push_front":
        dec.insert(0, lst[1])
    elif order == "pop_front":
        print(dec.pop(0) if len(dec) >= 1 else -1)
    elif order == "pop_back":
        print(dec.pop() if len(dec) >= 1 else -1)
    elif order == "size":
        print(len(dec))
    elif order == "empty":
        print(0 if len(dec) >= 1 else 1)
    elif order == "front":
        print(dec[0] if len(dec) >= 1 else -1)
    else:
        print(dec[-1] if len(dec) >= 1 else -1)
