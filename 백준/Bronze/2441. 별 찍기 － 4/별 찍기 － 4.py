N = int(input())
space = 0
for _ in range(N):
    print(' ' * space, end = '')
    print('*' * (N - space), end = '')
    print()
    space += 1