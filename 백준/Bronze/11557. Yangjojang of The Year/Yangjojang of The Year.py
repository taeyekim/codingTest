T = int(input())

for tc in range(1, T+1):
    word = ''
    max_V = -1
    N = int(input())
    for _ in range(N):
        A, B = input().split()
        if max_V <= int(B):
            word = A
            max_V = int(B)

    print(word)