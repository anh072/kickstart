# logn for update
def update1(val, i, left, right, tree, index):
    if i < left or i > right:
        return
    if left == right:
        tree[index] = (-1)**i * val
        return
    mid = left + (right-left)//2
    update1(val, i, left, mid, tree, 2*index+1)
    update1(val, i, mid+1, right, tree, 2*index+2)
    tree[index] = tree[2*index+1] + tree[2*index+2]


# logn for update
def update2(val, i, left, right, tree, index):
    if i < left or i > right:
        return
    if left == right:
        tree[index] = (-1)**i * val * (i+1)
        return
    mid = left + (right-left)//2
    update2(val, i, left, mid, tree, 2*index+1)
    update2(val, i, mid+1, right, tree, 2*index+2)
    tree[index] = tree[2*index+1] + tree[2*index+2]


# nlogn to build
def build1(arr, N):
    tree = [0] * (2*N-1)
    for i, val in enumerate(arr):
        update1(val, i, 0, N-1, tree, 0)
    return tree


# nlogn to build
def build2(arr, N):
    tree = [0] * (2*N-1)
    for i, val in enumerate(arr):
        update2(val, i, 0, N-1, tree, 0)
    return tree


def query_util(tree, qs, qe, ss, se, si):
    if qs > se or qe < ss:
        return 0
    if qs <= ss and qe >= se:
        return tree[si]
    mid = ss + (se-ss)//2
    left = query_util(tree, qs, qe, ss, mid, 2*si+1)
    right = query_util(tree, qs, qe, mid+1, se, 2*si+2)
    return left+right


def query(tree1, tree2, start, end, N):
    # (-1)^start * (tree2[start, end] - tree1[start, end] * start)
    val2 = query_util(tree2, start, end, 0, N-1, 0)
    val1 = query_util(tree1, start, end, 0, N-1, 0)
    return (-1)**start * (val2 - val1 * start)


def solve():
    N, Q = map(int, input().split())
    candies = [int(c) for c in input().split() ]
    # construct a segment tree (-1)^i A(i)
    tree1 = build1(candies, N)
    # construct a segment tree (-1)^i A(i)*i
    tree2 = build2(candies, N)
    ans = 0
    for i in range(Q):
        q, a, b = input().split()
        a, b = int(a), int(b)
        if q == "Q":
            ans += query(tree1, tree2, a-1, b-1, N)
        elif q == "U":
            update1(b, a-1, 0, N-1, tree1, 0)
            update2(b, a-1, 0, N-1, tree2, 0)
    return ans

T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))



