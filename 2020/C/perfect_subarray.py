def solve():
    N = int(input())
    arr = [int(c) for c in input().split(" ")]
    neg, pos = 0, 0
    for v in arr:
        if v > 0:
            pos += v
        else:
            neg -= v # note neg is positive
    occurences = [0] * (1+neg+pos)
    ans = 0
    pref_sum = 0
    occurences[neg] = 1
    for i in range(N):
        pref_sum += arr[i]
        j = 0
        while j*j <= pref_sum + neg:
            if neg + (pref_sum - j*j) >= 0:
                ans += occurences[neg + pref_sum - j*j]
            else:
                break
            j += 1
        occurences[neg + pref_sum] += 1
    return ans
    
T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))