n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
k = 0
sum = 0
for i in range(n):
    if lst[i] > 0:
        break
    k += 1
if m >= n:
    if k == 0:
        sum = lst[n - 1]
    elif k == n:
        sum = abs(lst[0])
    else:
        sum = abs(lst[0]) + lst[n - 1] + min(abs(lst[0]), lst[n - 1])
else:    
    if k == 0:
        for i in range(n - 1, -1, -m):
            sum += lst[i] * 2
        sum -= lst[n - 1]
    elif k == n:
        for i in range(0, n, m):
            sum += abs(lst[i]) * 2
        sum += lst[0]
    else:
        if k >= m:
            for i in range(0, k, m):
                sum += abs(lst[i]) * 2
        else:
            sum += abs(lst[0]) * 2
        if n - k >= m:
            for i in range(n - 1, k - 1, -m):
                sum += lst[i] * 2
        else:
            sum += lst[n - 1] * 2
        sum -= max(abs(lst[0]), lst[n - 1])
print(sum)