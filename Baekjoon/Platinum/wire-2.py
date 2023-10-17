from queue import PriorityQueue


class wire:
    def __init__(self, a, b, parent_wire):
        self.a = a
        self.b = b
        self.parent = parent_wire


def b_search(dp, wire, start, end):
    mid = (int)((start + end) / 2)
    if start > end:
        if start == len(dp):
            wire.parent = dp[-1]
            dp.append(wire)
        else:
            if dp[start].b > wire.b:
                wire.parent = dp[start - 1]
                dp[start] = wire
        return
    if dp[mid].b > wire.b:
        return b_search(dp, wire, start, mid - 1)
    else:
        return b_search(dp, wire, mid + 1, end)


wires = PriorityQueue()
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    wires.put((a, wire(a, b, None)))

result = {}
dp = [wire(-1, -1, None)]

for i in range(n):
    wire = wires.get()[1]
    result[f"{wire.a}"] = wire.a
    b_search(dp=dp, wire=wire, start=1, end=len(dp) - 1)


temp = dp[-1]
while temp.parent is not None:
    del result[f"{temp.a}"]
    temp = temp.parent

print(len(result))
for wire in result:
    print(wire)
