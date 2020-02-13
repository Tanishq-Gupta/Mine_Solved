l = int(input())
for j in range(l):
    a, b = list(map(int, input().split(' ')))
    bc, wc, n = list(map(int, input().split(' ')))
    price = a * bc + b * wc
    if ((a+b) * bc + (b * n)) < price:
        price = (a+b) * bc + (b * n)
    elif ((a+b) * wc + (a * n)) < price:
        price = (a+b) * wc + a * n
    print(price)