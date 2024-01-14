import sys
input = sys.stdin.readline
n = int(input())
if (n == 1):
    print(1)
    sys.exit(0)
lst = []
for i in range (1, n + 1):
    if (i % 2 == 0):
        lst.append(i)
index = 0
if (n % 2 == 0):
    while True:
        if (index % 2 == 1):
            lst.append(lst[index])
        index += 1
        if (index == len(lst)):
            break
else:
    while True:
        if (index % 2 == 0):
            lst.append(lst[index])
        index += 1
        if (index == len(lst)):
            break
print(lst[-1])