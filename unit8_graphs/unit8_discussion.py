"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""
from collections import deque

def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """
    # Return an empty list if the graph is empty or
    # the starting node does not exist in the graph.
    if not graph or start not in graph:
        return []

    # The visited set keeps track of nodes that have already
    # been discovered so they are not added to the queue again.
    visited = set()

    # BFS uses a queue (FIFO), so the first node added
    # is the first node processed. This allows BFS to
    # explore the graph level by level.
    queue = deque([start])

    visited.add(start)

    visited_order = []

    while queue:
        # Remove the first node from the queue.
        # This is what creates the FIFO behavior of BFS.
        current_node = queue.popleft()

        visited_order.append(current_node)

        # Add unvisited neighbors to the queue.
        # These neighbors will be processed after the
        # nodes already waiting in the queue.
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # BFS explores nearby nodes first, while DFS follows
    # one path as far as possible before backtracking.
    return visited_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")
    print("TODO: Create and display a graph.")

    # Nodes represent the people.
    # Edges represent the friendship connections between them.
    social_network = {
        "Amy": ["Bob", "Charlie", "Emily"],
        "Bob": ["Amy", "Charlie"],
        "Charlie": ["Amy", "Bob", "David"],
        "David": ["Charlie", "Emily", "Frank"],
        "Emily": ["David", "Frank"],
        "Frank": ["Emily", "David"]
    }

    print("\nSOCIAL NETWORK:")

    for person, friends in social_network.items():
        print(f"\n{person}:")
        for friend in friends:
            print(f"  -> {friend}")


    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")
    print("TODO: Perform and explain BFS traversal.")

    start_node = "Amy"

    traversal = bfs(social_network, start_node)

    print("\nSTARTING NODE:")
    print(start_node)
    print(f"\nTRAVERSAL ORDER: ")
    print(f"{' -> '.join(traversal)}")

    # BFS starts with Amy at Level 0.
    # Bob, Charlie, and Emily are directly connected to Amy,
    # so they are visited at Level 1.
    # David and Frank are reached through those Level 1 nodes,
    # so they are visited at Level 2.
    print("\nBFS LEVELS:")
    print("Level 0: Amy")
    print("Level 1: Bob, Charlie, Emily")
    print("Level 2: David, Frank")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.


    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    print("\nEDGE CASE 1: Use a disconnected node.")

    # Add Grace to the social network.
    # Grace has an empty list, meaning she has no connections
    # to any other person in the graph.
    social_network["Grace"] = []

    # Display all people in the social network.
    print("\nORIGINAL NETWORK AFTER ADDING 'GRACE':")
    for person, friends in social_network.items():
        print(f"{person}:")
        for friend in friends:
            print(f"  -> {friend}")

    # Display Grace's connections.
    # The empty list [] shows that Grace has no connections.
    print(f"\nGRACE's CONNECTIONS:", social_network["Grace"])

    # Run BFS starting from Amy.
    # BFS will visit everyone who can be reached from Amy.
    disconnected_result = bfs(social_network, "Amy")

    print("\nBFS STARTING FROM AMY:")
    print(f" -> ".join(disconnected_result))

    # Grace will NOT appear in the traversal because
    # there is no path connecting Amy to Grace.
    if "Grace" not in disconnected_result:
        print("\nGrace was NOT visited.")
        print("Grace is disconnected from Amy.")

    print("\nEDGE CASE 2: Handle a missing start node safely.")

    missing_start = "Zoe"

    missing_start_result = bfs(social_network, missing_start)

    print("\nBFS STARTING FROM ZOE:")

    if not missing_start_result:
        print("\nNo traversal was performed.")
        print(f"{missing_start} is NOT in the social network.")
    else:
        print(" -> ".join(missing_start_result))

if __name__ == "__main__":
    main()