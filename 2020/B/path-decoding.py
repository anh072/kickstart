def decode(s):
    stack = []
    for i in range(len(s)):
        if s[i] != "(" and s[i] != ")":
            stack.append(s[i])
        elif s[i] == ")":
            tmp = ""
            while not stack[-1].isdigit():
                tmp = stack.pop() + tmp # prepend
            d = int(stack.pop())
            tmp = d * tmp
            stack.append(tmp)
    return "".join(stack)


def solve():
    instructions = decode(input())
    current = [1, 1] # (col, row)
    ROWS = COLS = 10**9
    for c in instructions:
        if c == "N":
            current[1] += -1
        elif c == "S":
            current[1] += 1
        elif c == "W":
            current[0] += -1
        else:
            current[0] += 1
        
        if current[0] > COLS:
            current[0] = 1
        elif current[0] < 1:
            current[0] = COLS
        
        if current[1] > ROWS:
            current[1] = 1
        elif current[1] < 1:
            current[1] = ROWS
    return "{} {}".format(current[0], current[1])
            
    




T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))