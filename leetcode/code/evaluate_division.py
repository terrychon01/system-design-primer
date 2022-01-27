
import collections

def calcEquation(equations, values, queries):
    
    def dfs(graph, start, end, visited):
        
        if start == end and graph[start]:
            return 1.0
        
        visited.add(start)
        for neigh, val in graph[start]:
            if neigh in visited:
                continue
            
            tmp = dfs(graph, neigh, end, visited)
            if tmp > 0:
                return val * tmp
        
        return -1.0
        
    graph = collections.defaultdict(set)
    for items, v in zip(equations, values):
        x, y = items
        graph[x].add((y, v))
        graph[y].add((x, 1.0 / v))

    res = []
    for q in queries:
        res.append(dfs(graph, q[0], q[1], set()))

    return res

if __name__ == "__main__":
    
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    
    out = calcEquation(equations, values, queries)
    print(out)