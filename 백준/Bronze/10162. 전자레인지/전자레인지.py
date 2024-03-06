A = 300
B = 60
C = 10

t = int(input())

cnt_a, cnt_b, cnt_c = 0, 0, 0
while True:
    if t % 10 != 0:
        print(-1)
        break
    if t == 0:
        print(cnt_a, cnt_b, cnt_c)
        break
    
    if t >= A:
        t -= A
        cnt_a += 1
    elif t >= B:
        t -= B
        cnt_b += 1
    else:
        t -= C
        cnt_c += 1