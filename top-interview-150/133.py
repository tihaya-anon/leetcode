"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @classmethod
    def build_from_edges(cls, edges):
        nodes: dict[int, Node] = {}
        for f, t in edges:
            if f not in nodes:
                nodes[f] = Node(f)
            if t not in nodes:
                nodes[t] = Node(t)
            nodes[f].neighbors.append(nodes[t])
            nodes[t].neighbors.append(nodes[f])
        return nodes

    @classmethod
    def build_from_adj_list(cls, li):
        nodes: dict[int, Node] = {}
        for i, adj in enumerate(li):
            i += 1
            if i not in nodes:
                nodes[i] = Node(i)
            for n in adj:
                if n not in nodes:
                    nodes[n] = Node(n)
                nodes[i].neighbors.append(nodes[n])
        return nodes


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        visited = set()
        nodes: dict[int, Node] = {}

        def dfs(node: "Node"):
            if node.val in visited:
                return
            visited.add(node.val)
            if node.val not in nodes:
                nodes[node.val] = Node(node.val)
            for n in node.neighbors:
                dfs(n)
                nodes[node.val].neighbors.append(nodes[n.val])

        dfs(node)
        return nodes[1]


def print_graph(N, g):
    for i in range(N):
        i += 1
        print(g[i].val, end=" -> ")
        vals = []
        for n in g[i].neighbors:
            vals.append(n.val)
        print(vals)


adj_list = [[2, 4], [1, 3], [2, 4], [1, 3]]
N = len(adj_list)
graph = Node.build_from_adj_list(adj_list)
print_graph(N, graph)
new_graph = Solution().cloneGraph(graph[1])
print_graph(N, new_graph)
