h, m, s = map(int, input().split())

ps = int(input())
total = h * 3600 + m * 60 + s + ps
total %= 24 * 3600
h = total // 3600
total %= 3600
m = total // 60
total %= 60
s = total
print(h, m, s)