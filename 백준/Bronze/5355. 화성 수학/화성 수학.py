T = int(input())

for _ in range(T):
    lst = list(input().split())

    for i in range(len(lst)):
        if i == 0:
            total = float(lst[i])

        if lst[i] == '@' :
            total *= 3
        elif lst[i] == '%' :
            total += 5
        elif lst[i] == '#' :
            total -= 7
    print(f"{total:.2f}")