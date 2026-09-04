# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

This assignment gave me solid hands-on practice with recursive data structures,
which felt pretty different from the linear lists I'd worked with before. 
I got more comfortable writing methods that call themselves on smaller pieces of
the tree, and it clicked for me how much a tree's shape affects how efficiently
you can search it. I also finally understood why in-order traversal gives you
sorted output, it's really just a direct result of how values get placed during
insertion.

The trickiest part was making sure the recursive methods actually reconnected the
tree correctly after each call. Since _insert_recursive returns a node every 
time, I had to make sure each parent's pointer got updated with that return value,
otherwise nodes would get created but never actually attached anywhere. 
Tracing a few insertions by hand on paper helped a lot, following exactly which
pointer was being set at each step made the logic finally make sense. Testing an 
empty tree and a duplicate insertion also gave me more confidence that the base
cases were doing what I expected.

A BST follows one simple rule at every node: smaller values go left, larger values
go right, so comparing the target to the current node immediately tells you which
half to ignore, giving a balanced tree O(log n) search time. A plain list has no
such ordering, so a linear search checks items one by one, O(n) in the worst case.
A sorted array can also hit O(log n) with binary search, but inserting or deleting
means shifting elements to keep everything in order, something a BST avoids since
it just attaches a new node wherever it belongs. The catch is that a BST only stays
fast if it stays balanced, insert values in the wrong order, and it can skew heavily
to one side, dragging performance back down to O(n), basically acting like a linked
list at that point.