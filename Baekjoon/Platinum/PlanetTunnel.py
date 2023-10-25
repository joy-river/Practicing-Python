class Planet:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def cost(self, p):
        return min(abs(p.x - self.x), abs(p.y - self.y), abs(p.z - self.z))


class UF_tree:
    def __init__(self, index, planet) -> None:
        self.index = index
        self.planet = planet
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
            return


n = int(input())
