import sys
input = sys.stdin.readline


def find(i):
    if parent[i] == i:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]


def union(p1, p2):
    p1_root = find(p1)
    p2_root = find(p2)

    if p1_root == p2_root:
        return False

    if p1_root <= p2_root:
        parent[p2_root] = p1_root
        return True
    else:
        parent[p1_root] = p2_root
        return True


n = int(input())
planets = []
parent = [i for i in range(n)]

v = []
total_cost = 0

for i in range(n):
    x, y, z = list(map(int, input().split()))
    planets.append((i, x, y, z))

for i in [1, 2, 3]:
    sort = sorted(planets, key=lambda x: x[i])
    for a, b in zip(sort[:-1], sort[1:]):
        v.append((abs(b[i] - a[i]), (a[0], b[0])))

v.sort()
cnt = 0

for tunnel in v:
    p1 = tunnel[1][0]
    p2 = tunnel[1][1]
    if union(p1, p2):
        cnt += 1
        total_cost += tunnel[0]
    if cnt == n - 1:
        break

print(total_cost)
