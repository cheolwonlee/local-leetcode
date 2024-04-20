"""There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1

Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2

Constraints:

    1 <= n <= 100
    0 <= edges.length <= n * (n - 1) / 2
"""
from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pass

tests=[
    (
        (3,[[0,1], [0,2]],),
        1
    ),(
        (6,[[0,1], [1,2], [2,3], [4,5]]),
        2
    )
]
        
        