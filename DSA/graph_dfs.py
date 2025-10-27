"""
Graph Depth-First Search (DFS)

Implementation of Depth-First Search algorithm for graph traversal.
"""

def dfs(graph, start, visited=None):
    """
    Perform depth-first search on a graph.
    
    Args:
        graph: Dictionary representing adjacency list of the graph
        start: Starting vertex
        visited: Set of visited vertices
        
    Returns:
        List of vertices in DFS order
    """
    if visited is None:
        visited = set()
    
    result = [start]
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Test cases
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("DFS starting from vertex 'A':", dfs(graph, 'A'))