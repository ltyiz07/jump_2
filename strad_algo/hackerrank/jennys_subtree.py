#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jennysSubtrees' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER r
#  3. 2D_INTEGER_ARRAY edges
#
def get_my_tree(edges):
    my_tree = dict()
    # Write your code here
    for edge in edges:
        if my_tree.get(edge[0]):
            my_tree[edge[0]].add(edge[1])
        else:
            my_tree[edge[0]] = {edge[1]}
        if my_tree.get(edge[1]):
            my_tree[edge[1]].add(edge[0])
        else:
            my_tree[edge[1]] = {edge[0]}
    return my_tree

def check_isomorphic(tree_1, tree_2):
    first_order = [len(nodes_set) for nodes_set in tree_1].sort()
    second_order = [len(nodes_set) for nodes_set in tree_1].sort()
    return first_order == second_order

def get_graph_order(graph):
    tuple([len(nodes_set) for nodes_set in graph].sort())


def jennysSubtrees(n, r, edges):
    my_tree = get_my_tree(edges)
    print(f"my_tree: {my_tree}")
    graph_order_set = set()

    def dfs(depth, pool):
        if depth == 1:
            return pool
        else:
            for node in pool.copy():
                pool = pool.union(my_tree[node])
            return dfs(depth-1, pool)

    for x in my_tree.keys():
        # sorted_order = sorted([len(my_tree[s]) for s in dfs(r, {x}) if len(my_tree[s]) != 1])
        print(dfs(r, {x}))
        sorted_order = sorted([len(my_tree[s]) for s in dfs(r, {x})])
        graph_order_set.add(tuple(sorted_order))
        # graph_order_set.add(dfs(n, {x}))
    print(graph_order_set)
    return len(graph_order_set)

if __name__ == '__main__':
    # assert jennysSubtrees(7, 1, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]) == 3, (jennysSubtrees(7, 1, [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7]]))
    # assert jennysSubtrees(7, 3, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]) == 4

    print(f"answer: {jennysSubtrees(20, 9, [[1, 19], [12, 8], [3, 9], [10, 2], [13, 7], [17, 4], [14, 18], [14, 16], [20, 6], [2, 3], [6, 15], [16, 1], [5, 9], [4, 16], [3, 18], [12, 4], [11, 20], [2, 7], [11, 16]])}")
    """
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    r = int(first_multiple_input[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = jennysSubtrees(n, r, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
    """

[[20, 9], [1, 19], [12, 8], [3, 9], [10, 2], [13, 7], [17, 4], [14, 18], [14, 16], [20, 6], [2, 3], [6, 15], [16, 1], [5, 9], [4, 16], [3, 18], [12, 4], [11, 20], [2, 7], [11, 16]]
