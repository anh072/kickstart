def recurse(index, taken, k, acc_sum, num_stacks, P, cache):
    if taken == P:
        return 0
    if index >= num_stacks or taken > P:
        return -10**10
    if cache[index][taken] != -1:
        return cache[index][taken]
    ans = 0
    for i in range(k+1):
        ans = max(
            ans, 
            acc_sum[index][i] + recurse(index+1, taken+i, k, acc_sum, num_stacks, P, cache)
        )
    cache[index][taken] = ans
    return ans


def solve():
    num_stacks, num_plates, P = map(int, input().split(" "))
    acc_sum = [[0 for i in range(num_plates+1)] for j in range(num_stacks)]
    cache = [[-1 for i in range(P+1)] for j in range(num_stacks)]
    for k in range(num_stacks):
        arr = [int(val) for val in input().split(" ")]
        for j in range(num_plates):
            acc_sum[k][j+1] = acc_sum[k][j] + arr[j]
    return "{}".format(recurse(0, 0, num_plates, acc_sum, num_stacks, P, cache))


t = int(input())
for c in range(t):
	print("Case #{}: {}".format(c+1, solve()))