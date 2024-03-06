T = int(input())
Yonsei = 0
Korea = 0
for tc in range(1, T+1):
    for i in range(9):
        a, b = map(int, input().split())
        Yonsei += a
        Korea += b
    if Yonsei > Korea:
        print("Yonsei")
    elif Yonsei < Korea:
        print("Korea")
    else:
        print("Draw")