T = int(input())

Chang = 100
Sang = 100
for tc in range(1, T+1):
    c, s = map(int, input().split())
    
    V = max(c,s)
    if c == s:
        continue
    elif V == c:
        Sang -= c
    else:
        Chang -= s
    
print(Chang)
print(Sang)