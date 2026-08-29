# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

This assignment reinforced how Python lists actually behave when
you insert, delete, or search for values. Implementing insert_at
and delete_at made it clear that both operations rely on shifting
elements in memory to keep the list contiguous, which is why 
performance depends heavily on where the operation happens, 
not just what it does. Inserting or deleting near the end stays 
close to O(1), while doing either near the beginning forces nearly
every element to shift, making it O(n).

The main challenge was handling invalid indices safely. Rather than
letting the program crash with an IndexError, I added bounds checks
that return None for a bad delete or -1 for a failed search, which
forced me to think about failure cases up front instead of only the
expected path.

In real-world applications, these tradeoffs matter constantly. 
Systems that frequently insert or remove from the front of large
lists (like task queues or live feeds) perform far better with 
structures built for that access pattern, while linear search 
becomes a real bottleneck as data grows, which is why sorted 
structures or hash-based lookups are often used instead.