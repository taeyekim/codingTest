T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    ans = 0
    if A == 1 or B == 1:
        ans = max(A, B)
    else:
        for i in range(min(A, B), A*B + 1, min(A, B)):
            if i % A == 0 and i % B == 0:
                ans = i
                break
    print(ans)