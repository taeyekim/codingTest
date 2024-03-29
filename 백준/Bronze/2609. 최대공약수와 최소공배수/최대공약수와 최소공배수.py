A, B = map(int, input().split())
a = A
b = B

while b != 0:
    a, b = b, a%b
ans1 = a
ans2 = A*B//ans1

print(ans1)
print(ans2)