from heapq import heapify, heappop, heappush

def solve():
    N, K = map(int, input().split(" "))
    sessions = [int(val) for val in input().split(" ")]
    diff = [0] * N
    for i in range(1, N):
        diff[i] = sessions[i-1] - sessions[i] # by default, heapq is min heap
    heapify(diff)
    while -1 * diff[0] > 1 and K > 0:
        largest = -1 * heappop(diff)
        mid = largest // 2
        first, second = mid, largest - mid
        heappush(diff, -first)
        heappush(diff, -second)
        print(diff)
        K -= 1
    if K == 0:
        return "{}".format(-1 * heappop(diff))
    return "1"


t = int(input())
for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))