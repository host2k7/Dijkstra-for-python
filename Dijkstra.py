import math
def dijkstra(node, last, graph, check, checkpoint, visited = None, road = None):
    if visited is None:
        visited = set()
    if road is None:
        road = []    
        
    visited.add(node)
    road.append(node)
        
    min_value = math.inf
    min_child = None
    
    for par in graph[node]: #check the following point to come
        if par not in visited: # check if the point was in visited or not
            if checkpoint[par] > check[str(node) + " " + str(par)] + checkpoint[node]:
                # update the point value
                checkpoint[par] = check[str(node) + " " + str(par)] + checkpoint[node]
            if par == last:
                # if the point == to the goal, return the list contain the road
                road.append(last)
                print(checkpoint[last])
                return road
            if checkpoint[par] < min_value:
                # if not, choose the min value and countinue
                min_value = checkpoint[par]
                min_child = par
    
    if min_child is not None:
        return dijkstra(min_child,last,graph,check,checkpoint,visited,road)
    
    return road