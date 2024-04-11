N = int(input())
star = N * 2 - 1
space = 0
for i in range(N):
    print(' ' * space, end = '')
    print('*' * star, end = '')
    print()
    star -= 2
    space += 1