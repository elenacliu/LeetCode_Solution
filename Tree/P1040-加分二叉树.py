# n为结点总数
from functools import lru_cache

n = int(input())
# scores为各节点的分数
scores = input().split()
scores = [int(scores[i]) for i in range(n)]

assert n > 0


class Node:
    def __init__(self, index, score=1):
        self.lc = None
        self.rc = None
        self.index = index
        self.weight = score

    def __str__(self):
        return str(self.index)


nodes = [Node(index=i+1, score=scores[i]) for i in range(n)]
f = [[0 for _ in range(n)] for _ in range(n)]


@lru_cache(maxsize=512)
def calc_max_scores(left, right):
    global count
    # print('left: ', left, ' right: ', right)
    if left > right:
        return 1
    if left == right:
        f[left][right] = left
        return scores[left]

    tmp, index = 0, -1

    for i in range(left, right+1):
        res_lc = calc_max_scores(left, i-1)
        res_rc = calc_max_scores(i+1, right)
        new_temp = res_lc * res_rc + nodes[i].weight
        if new_temp > tmp:
            index = i
            tmp = new_temp

    assert index != -1
    f[left][right] = index

    return tmp


res = calc_max_scores(0, n-1)
print(res)


def print_res(left, right):
    if left > right:
        return
    print(f[left][right] + 1, end=" ")
    if left == right:
        return
    print_res(left, f[left][right] - 1)
    print_res(f[left][right] + 1, right)


print_res(0, n-1)
