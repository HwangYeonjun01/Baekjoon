import sys
input = sys.stdin.readline
n, k = map(int, input().split())
if (n == 1):
    print("<1>")
    sys.exit(0)
lst1 = []
lst2 = []
for i in range (1, n + 1):
    lst1.append(i)
count = 1
while True:
    if len(lst2) == n:
        break
    if (count % k == 0):
        lst2.append(str(lst1[count - 1]))
    else:
        lst1.append(lst1[count - 1])
    count += 1
str = "<"
for i in range(n - 1):
    str += lst2[i] + ", "
str += lst2[n - 1] + ">"
print(str)