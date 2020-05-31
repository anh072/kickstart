# logn for update
def update(mode, val, i, left, right, tree, index):
    if i < left or i > right:
        return
    if left == right:
        if mode == "S":
            tree[index] = (-1)**i * val
        else:
            tree[index] = (-1)**i * val * (i+1)
        return
    mid = left + (right-left)//2
    update(mode, val, i, left, mid, tree, 2*index+1)
    update(mode, val, i, mid+1, right, tree, 2*index+2)
    tree[index] = tree[2*index+1] + tree[2*index+2]


def build_util(mode, tree, ss, se, arr, si):
    if ss == se:
        if mode == "S":
            tree[si] = (-1)**ss * arr[ss]
        else:
            tree[si] = (-1)**ss * arr[ss] * (ss+1)
        return
    mid = ss + (se-ss)//2
    build_util(mode, tree, ss, mid, arr, 2*si+1)
    build_util(mode, tree, mid+1, se, arr, 2*si+2)
    tree[si] = tree[2*si+1] + tree[2*si+2]


# O(n) to build
def build(arr, N, mode):
    tree = [0] * (2*N-1)
    build_util(mode, tree, 0, N-1, arr, 0)
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
    tree1 = build(candies, N, "S")
    # construct a segment tree (-1)^i A(i)*i
    tree2 = build(candies, N, "M")
    ans = 0
    for i in range(Q):
        q, a, b = input().split()
        a, b = int(a), int(b)
        if q == "Q":
            ans += query(tree1, tree2, a-1, b-1, N)
        elif q == "U":
            update("S", b, a-1, 0, N-1, tree1, 0)
            update("M", b, a-1, 0, N-1, tree2, 0)
    return ans

T = int(input())
for c in range(T):
    print("Case #{}: {}".format(c+1, solve()))



