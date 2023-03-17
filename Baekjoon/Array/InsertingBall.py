nm = input().split(" ")
n = int(nm[0])
m = int(nm[1])

basket = [0 for i in range(n)]

for repeat in range(m):
    insert = input().split(" ")
    for a in range(int(insert[0]) - 1, int(insert[1])):
        basket[a] = int(insert[2])

print(*basket)
