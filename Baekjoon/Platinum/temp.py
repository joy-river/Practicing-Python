from queue import PriorityQueue


class UF_tree:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.rank = 0
        self.parent = self

    def find(self):
        if self.parent == self:
            return self
        else:
            self.parent = self.parent.find()
            return self.parent

    def union(self, node):
        self_root = self.find()
        node_root = node.find()

        if self_root == node_root:
            return False

        if self_root.rank < node_root.rank:
            self_root.parent = node_root
            return True
        else:
            node_root.parent = self_root
            if self_root.rank == node_root.rank:
                self_root.rank += 1
            return True


n = int(input())
planets = []
v = PriorityQueue()
vx = PriorityQueue()
vy = PriorityQueue()
vz = PriorityQueue()
total_cost = 0

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append(UF_tree(x, y, z))
    vx.put((x, i))
    vy.put((y, i))
    vz.put((z, i))

x = vx.get()
y = vy.get()
z = vz.get()

while not vx.empty():
    x2 = vx.get()
    y2 = vy.get()
    z2 = vz.get()

    v.put((abs(x2[0] - x[0]), (x[1], x2[1])))
    v.put((abs(y2[0] - y[0]), (y[1], y2[1])))
    v.put((abs(z2[0] - z[0]), (z[1], z2[1])))

    x = x2
    y = y2
    z = z2

while not v.empty():
    tunnel = v.get()
    p1 = planets[tunnel[1][0]]
    p2 = planets[tunnel[1][1]]

    if p1.union(p2):
        total_cost += tunnel[0]

print(total_cost)
