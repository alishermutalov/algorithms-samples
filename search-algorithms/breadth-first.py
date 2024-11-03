from collections import deque

def search(start_node:str, target:str, graph:dict)->bool:
    """
    Perform a breadth-first search (BFS) to determine if the target node exists 
    in the graph starting from the given start node.

    Args:
        start_node (str): The node from which the search begins.
        target (str): The value or node to search for in the graph.
        graph (dict): A dictionary representing the graph structure, where 
                      keys are nodes and values are lists of adjacent nodes.

    Returns:
        bool: True if the target node is found in the graph, False otherwise.

    Example:
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': [],
            'F': []
        }

        result = search('A', 'E', graph)  # Returns True
        result = search('A', 'G', graph)  # Returns False

    Algorithm:
        1. Initialize a deque `search_queue` and add the neighbors of `start_node`.
        2. Create an empty set `searched` to track visited nodes and avoid revisiting them.
        3. While `search_queue` is not empty:
            a. Dequeue the leftmost node from `search_queue`.
            b. If the node has not been searched:
                i. If the node matches the `target`, return True.
                ii. Otherwise, add its neighbors to `search_queue` and mark the node as searched.
        4. If the queue is exhausted without finding the target, return False.

    Notes:
        - The function ensures that each node is only visited once by using the `searched` set.
        - The BFS approach guarantees the shortest path is found if the target is reachable.
        - The function can handle cyclic graphs by avoiding revisiting already searched nodes.
    """
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()
    
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person==target:
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
                
    return False
    
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

print(search('A', 'E', graph))  # Output: True