# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

Working through this assignment helped me better understand how graphs are represented 
using adjacency lists and how Breadth-First Search (BFS) moves through them level-by-level.
Implementing BFS also made it clearer to me why a queue (FIFO) is used to keep track
of which nodes should be visited next. I also gained more practice using a visited
set to make sure nodes are not processed more than once. Working with edge cases,
such as disconnected nodes and invalid starting points, helped me understand how to
make the algorithm handle different situations safely.

2. What challenges did you encounter, and how did you overcome them?

One challenge I had was understanding the order in which nodes are added to and removed
from the queue. At first, it was a little confusing to see how BFS keeps track of each
level. I worked through the graph step-by-step and followed the queue after each node
was processed. This helped me understand why neighbors are added to the queue and how
the algorithm moves from one level to the next. Testing the code with different starting
points also helped me make sure the traversal was working correctly.

3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

BFS uses a queue to explore a graph level-by-level, starting with the closest neighbors
before moving farther away. Depth-First Search (DFS), on the other hand, uses a stack
or recursion to follow one path as far as possible before backtracking. BFS can be
useful for finding the shortest path in an unweighted graph, such as finding connections
between people on a social network. DFS can be useful for exploring mazes, directories,
decision trees, or checking connected components in a graph.
