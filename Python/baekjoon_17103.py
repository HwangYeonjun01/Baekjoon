lst = [True] * 1000001
lst[0] = lst[1] = False
for i in range(2, 1001):
    if lst[i]:
        for j in range(2 * i, 1000001, i):
            lst[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for i in range(2, n // 2 + 1):
        if lst[i] and lst[n - i]:
            count += 1
    print(count)