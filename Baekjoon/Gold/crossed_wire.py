from queue import Queue


def b_search(dp, wire, start, end):
    mid = (int)((start + end) / 2)
    if start > end:
        if start == len(dp):
            dp.append(wire)
        else:
            if dp[start] > wire:
                dp[start] = wire
        return
    if dp[mid] > wire:
        return b_search(dp, wire, start, mid - 1)
    else:
        return b_search(dp, wire, mid + 1, end)


wires = Queue()
n = int(input())
w_input = input().split()
for i in range(n):
    a = int(w_input[i])
    wires.put(a)

dp = [-1]

for i in range(n):
    wire = wires.get()
    b_search(dp=dp, wire=wire, start=1, end=len(dp) - 1)


print(len(dp) - 1)
