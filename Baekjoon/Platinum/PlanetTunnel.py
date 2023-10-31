
from queue import PriorityQueue


class UF_tree:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.rank = 0
        self.parent = self

    def cost(self, p):
        return min(abs(p.x - self.x), abs(p.y - self.y), abs(p.z - self.z))

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
            return

        if self_root.rank < node_root.rank:
            self_root.parent = node_root
        else:
            node_root.parent = self_root
            if self_root.rank == node_root.rank:
                self_root.rank += 1


n = int(input())
planets = []
v = PriorityQueue()
total_cost = 0

for i in range(n):
    x, y, z = map(int, input().split())
    planets.append(UF_tree(x, y, z))

while not v.empty():
    tunnel = v.get()
    p1 = planets[tunnel[1][0]]
    p2 = planets[tunnel[1][1]]
    if p1.find() != p2.find():
        p1.union(p2)
        total_cost += tunnel[0]

print(total_cost)
