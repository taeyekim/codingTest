h, m = map(int, input().split())

pm = int(input())

total = h * 60 + m + pm
total %= 1440
answer_h = total // 60
answer_m = total % 60
print(answer_h, answer_m)
