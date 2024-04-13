colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
values = [1]
total = ''
for i in range(1, 10):
    values.append(values[i-1] * 10)
color = input()
total += str(colors.index(color))
color = input()
total += str(colors.index(color))
color = input()
total = int(total)
total *= values[colors.index(color)]
print(total)
