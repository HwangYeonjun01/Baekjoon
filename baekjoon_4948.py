import math

lst = [True for i in range(2 * 123456 + 1)]
lst[0], lst[1] = False, False
for i in range(2, int(math.sqrt(2 * 123456)) + 1):
    if lst[i]:
        j = 2
        while i * j <= 2 * 123456:
            lst[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if lst[i]:
            count += 1
    print(count)