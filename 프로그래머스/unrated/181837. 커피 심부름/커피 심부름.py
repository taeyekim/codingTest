def solution(order):
    total = 0
    for i in order:
        if "americano" in i:
            total += 4500
        elif "cafelatte" in i:
            total += 5000
        else:
            total += 4500
    return total