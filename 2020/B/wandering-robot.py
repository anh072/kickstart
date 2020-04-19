from collections import defaultdict

def in_hole(col, row, L, U, R, D):
    return (L <= col <= R and U <= row <= D) \
        or (col < 1) or (row < 1)

def solve():
    origin = (1, 1)
    W, H, L, U, R, D = map(int, input().split(" "))
    dp = defaultdict(int)
    dp[(1,1)] = 1

    for i in range(1, W+1): # COL
        for j in range(1, H+1): # ROW
            if not in_hole(i, j, L, U, R, D):
                prob1 = dp[(i-1, j)] # left
                prob2 = dp[(i, j-1)] # above
                dp[(i, j)] += prob1 * 1 if j == H else prob1 * 0.5 # bottom row
                dp[(i, j)] += prob2 * 1 if i == W else prob2 * 0.5 # right most col
    return dp[(W, H)]

T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))