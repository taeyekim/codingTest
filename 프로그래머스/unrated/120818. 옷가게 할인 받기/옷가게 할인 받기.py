def solution(price):
    sale_rate = 0
    if price >= 500000:
        sale_rate = 0.2
    elif price >= 300000:
        sale_rate = 0.1
    elif price >= 100000:
        sale_rate = 0.05
    answer = price * (1 - sale_rate)
    return int(answer)