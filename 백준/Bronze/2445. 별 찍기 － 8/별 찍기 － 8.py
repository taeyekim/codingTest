N = int(input())
star = 1
space = N * 2 - star * 2
for i in range(N - 1):
    print('*' * star, end = '')
    print(' ' * space, end = '')
    print('*' * star)
    star += 1
    space -= 2
print('*' * (star * 2))
for i in range(N - 1):
    star -= 1
    space += 2
    print('*' * star, end = '')
    print(' ' * space, end = '')
    print('*' * star)
