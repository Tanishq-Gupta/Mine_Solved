n = int(input())
l = list(map(int, input().split(' ')))
c = []
for i in l:
    if i not in c:
        c.append(i)
for i in range(0, len(c)):
    m = min(l)
    for j in range(0, len(l)):
        l[j] -= m
    k = len(l)
    while 0 in l:
        l.remove(0)
    print(k)