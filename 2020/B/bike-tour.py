
def solve():
    N = int(input())
    checkpoints = input().split(" ")
    for j in range(N):
        checkpoints[j] = int(checkpoints[j])
    i = 1
    count = 0
    while i <= N-2:
        if checkpoints[i] > checkpoints[i-1] and checkpoints[i] > checkpoints[i+1]:
            count += 1
            i += 2
        else:
            i += 1
    return count


T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))