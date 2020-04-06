
def solve():
    num_stacks, num_plates, P = map(int, input().split(" "))
    stacks = []
    for i in range(num_stacks):
        stack = [int(val) for val in input().split(" ")]
        stacks.append(stack)
    

t = int(input())
for c in range(t):
    print("Case #{}: {}".format(c+1, solve()))