
def solve():
    N, D = map(int, input().split(" "))
    freq = input().split(" ")
    ans = D
    for i in range(N-1, -1, -1):
        freq[i] = int(freq[i])
        result = (ans // freq[i]) * freq[i]
        ans = min(ans, result)
    return ans

T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))