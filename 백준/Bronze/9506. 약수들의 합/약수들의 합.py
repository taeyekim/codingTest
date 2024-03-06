while True:
    num = int(input())
    if num == -1:
        break
    arr = []
    for i in range(1, num // 2 + 1):

        if num % i == 0:
           arr.append(i)
    if sum(arr) == num:
        print(num, end = " = ")
        for i in range(len(arr)):
             print(f"{arr[i]} ", end = "")
             if arr[i] != arr[-1]:
                 print("+ ", end = '')
    else:
        print(f"{num} is NOT perfect.")