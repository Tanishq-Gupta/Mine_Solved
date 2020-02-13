n = int(input())
u = 0
p = ""
for a in range(n):
    c = 0
    p = ""
    count = 0
    v, x = list(map(int, input().split(' ')))
    for i in range(v, x+1):
        p = ""
        k = i**0.5
        k = str(k)
        c = 0
        for j in range(len(k)):
            if k[j] == '.':
                if k[j+1] == '0':
                    for q in range(j+1, len(k)):
                        p += k[q]
        if len(p) == 1 and p[0] == '0':
            count += 1
    print(count)