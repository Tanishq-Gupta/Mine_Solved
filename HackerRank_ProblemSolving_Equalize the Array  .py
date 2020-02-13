n = int(input())
l = list(map(int, input().split(' ')))
c_array = [0]*101
for i in range(len(l)):
    c_array[l[i]] += 1
print(len(l)-max(c_array))