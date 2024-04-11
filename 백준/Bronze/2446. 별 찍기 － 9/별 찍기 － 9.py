N = int(input())
star = N * 2 - 1
space = 0
for i in range(N - 1):
    print(' ' * space, end = '')
    print('*' * star)
    star -= 2
    space += 1
print(' ' * space, end = '')
print('*' * star)

for i in range(N - 1):
    star += 2
    space -= 1
    print(' ' * space, end = '')
    print('*' * star)
