import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst2 = list(set(lst))
lst2.sort()
dic = {}
for i in range(len(lst2)):
    dic[lst2[i]] = i
for i in lst:
    print(dic[i], end=" ")