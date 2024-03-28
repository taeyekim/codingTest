T = int(input())
cnt1 = 0
cnt0 = 0
for tc in range(1, T+1):
    answer = int(input())
    if answer == 1:
        cnt1 += 1
    else:
        cnt0 += 1

if cnt1 > cnt0:
    print('Junhee is cute!')
elif cnt1 < cnt0:
    print('Junhee is not cute!')