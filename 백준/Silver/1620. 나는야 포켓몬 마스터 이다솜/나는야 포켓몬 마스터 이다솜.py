N, M = map(int, input().split())
name_vs_number = {}
number_vs_name = {}
for i in range(N):
    name = input()
    number = i + 1
    name_vs_number[name] = number
    number_vs_name[number] = name

for _ in range(M):
    q = input()
    if q.isdigit():
        print(number_vs_name[int(q)])
    else:
        print(name_vs_number[q])
