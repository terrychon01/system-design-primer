'''
You are given an array routes representing bus routes where routes[i] 
is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], 
this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.

You will start at the bus stop source (You are not on any bus initially), 
and you want to go to the bus stop target. 

You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. 

Return -1 if it is not possible.
'''

import collections

def buses_destination(routes, S, T):
    
    if S == T: 
        return 0
    
    queue = collections.deque()
    graph = collections.defaultdict(set)
    routes = list(map(set, routes))
    
    seen = set()
    targets = set()
    
    for i in range(len(routes)):
        # print(i)
        if S in routes[i]:  # possible starting route number
            seen.add(i)
            queue.append((i, 1))  # enqueue
        if T in routes[i]:  # possible ending route number
            targets.add(i)
        for j in range(i+1, len(routes)):
            if routes[j] & routes[i]:  # set intersection to check if route_i and route_j are connected
                graph[i].add(j)
                graph[j].add(i)
                
    # print(graph)
    # print(queue)
    
    while queue:
        cur, count = queue.popleft()
        if cur in targets:
            return count
        for nei in graph[cur]:
            if nei not in seen:
                queue.append((nei, count+1))
                seen.add(nei)
    return -1


if __name__ == "__main__":
    
    routes = [[1,2,7],
              [3,6,7]]
    
    S = 1
    T = 6
    
    out = buses_destination(routes, S, T)
    print(out)