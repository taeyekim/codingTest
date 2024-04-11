N = int(input())

star = 1
space = (N * 2 - 1) // 2
for _ in range(N - 1):
    print(' ' * space, end = '')
    print('*' * star)
    space -= 1
    star += 2

star = N * 2 - 1
space = 0
for i in range(N * 2 - 1):
    print(' ' * space, end = '')
    print('*' * star)
    star -= 2
    space += 1