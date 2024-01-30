def solution(n):
    i = n + 1
    for i in range(n+1, n*2):
        if bin(n)[2:].count('1') == bin(i)[2:].count('1'):
            return i