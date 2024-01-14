import sys
input = sys.stdin.readline
n = int(input())
lst = []
cnt = 0
for i in range(n):
    a = input()
    if a[:4] == "push":
        lst.append(a[5:len(a) - 1])
    elif a[:3] == "pop":
        if (len(lst) == cnt):
            print(-1)
        else: 
            print(lst[cnt])
            cnt += 1
    elif a[0] == "s":
        print(len(lst) - cnt)
    elif a[0] == "e":
        print(1 if len(lst) == cnt else 0)
    elif a[0] == "f":
        print(-1 if (len(lst) == cnt) else lst[cnt])
    else:
        print(-1 if (len(lst) == cnt) else lst[len(lst) - 1])