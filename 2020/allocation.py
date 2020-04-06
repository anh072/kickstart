from heapq import heapify, heappop

def solve():
    num_houses, budget = map(int, input().split(" "))
    prices = [int(val) for val in input().split(" ")]
    heapify(prices)
    count = 0
    while len(prices):
        cheapest = heappop(prices)
        if cheapest > budget:
            break
        count += 1
        budget -= cheapest
    return "{}".format(count)

t = int(input())
for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))