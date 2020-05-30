

def solve():
    s = input()
    ptr = [0]
    M = 10**9

    def helper(ptr):
        r = [0, 0] # col ,row
        while ptr[0] < len(s):
            if s[ptr[0]] == ")":
                ptr[0] += 1
                break
            elif s[ptr[0]] == "N":
                r[1] += -1
                if r[1] < 0:
                    r[1] += M
                ptr[0] += 1
            elif s[ptr[0]] == "S":
                r[1] += 1
                if r[1] >= M:
                    r[1] -= M
                ptr[0] += 1
            elif s[ptr[0]] == "W":
                r[0] += -1
                if r[0] < 0:
                    r[0] += M
                ptr[0] += 1
            elif s[ptr[0]] == "E":
                r[0] += 1
                if r[0] >= M:
                    r[0] -= M
                ptr[0] += 1
            else:
                d = int(s[ptr[0]])
                ptr[0] += 2
                b = helper(ptr)
                r[0] = (r[0] + d*b[0]) % M
                r[1] = (r[1] + d*b[1]) % M
        return r

    ans = helper(ptr)
    return "{} {}".format(ans[0]+1, ans[1]+1)
            
T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))