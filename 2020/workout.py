# f(d) = number of additional sessions at difficulty d
# f(d) = sum((sessions[i] - sessions[i-1] -1) // d)
# d is valid when f(d) <= k
# possible range for d = [1, 10**9]
# if m is valid, for x > m, f(x) < f(m) <= k => ignore the right half because we want to find the maximum d
# if m is not valid, for x < m, f(x) > f(m) >= k => ignore the left half because it is not valid

def is_valid(d, K, sessions):
    additional_sessions = 0
    for i in range(1, len(sessions)):
        additional_sessions += (sessions[i] - sessions[i-1] - 1) // d
    if additional_sessions <= K:
        return True
    return False

def bin_search(low, high, K, sessions):
    while low < high:
        mid = (low + high) // 2
        if is_valid(mid, K, sessions):
            high = mid
        else:
            low = mid + 1
    return low


def solve():
    N, K = map(int, input().split(" "))
    sessions = [int(val) for val in input().split(" ")]
    return "{}".format(bin_search(1, 10**9-1, K, sessions))


t = int(input())
for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))