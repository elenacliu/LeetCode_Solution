from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(set)
        weight = defaultdict()

        for idx, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            weight[tuple(equ)] = values[idx]
            weight[(equ[1], equ[0])] = float(1 / values[idx])

        def dfs(start, end, visited):
            if (start, end) in weight:
                return weight[(start, end)]
            if start not in graph or end not in graph:
                return 0
            if start in visited:
                return 0
            visited.add(start)
            res = 0
            for tmp in graph[start]:
                res = (dfs(tmp, end, visited) * weight[(start, tmp)])
                if res != 0:
                    weight[(start, end)] = res
                    break
            visited.remove(start)
            return res

        res = []
        for q in queries:
            tmp = dfs(q[0], q[1], set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res