N = int(input())
star = 1

for i in range(N):
    space = ((N * 2 - star) // 2)
    print(' ' * (space), end = '')
    print('*' * star, end = '')
    print()
    star += 2