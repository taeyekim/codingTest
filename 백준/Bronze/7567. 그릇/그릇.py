pre_s = ''
cnt = 0
s = input()
for c in s:
    if pre_s == c:
        cnt += 5
    else:
        cnt += 10
    pre_s = c
print(cnt)