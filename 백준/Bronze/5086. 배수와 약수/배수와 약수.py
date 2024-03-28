while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    if A % B == 0:
        ans = 'multiple'
    elif B % A == 0:
        ans = 'factor'
    else:
        ans = 'neither'
    print(ans)