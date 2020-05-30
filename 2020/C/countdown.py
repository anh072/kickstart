def solve():
    N, K = map(int, input().split(" "))
    ans = 0
    arr = [int(c) for c in input().split(" ")]
    next = -1
    for d in arr:
        if d == K:
            next = K-1
        else:
            if d != next:
                next = -1
            else:
                if next == 1:
                    ans += 1
                    next = -1
                else:
                    next -= 1
    return ans        
     
T = int(input())
 
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))