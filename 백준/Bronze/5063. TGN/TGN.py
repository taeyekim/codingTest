N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())

    if r < e - c:
        ans = 'advertise'
    elif r > e - c:
        ans = 'do not advertise'
    else:
        ans = 'does not matter'
    print(ans)