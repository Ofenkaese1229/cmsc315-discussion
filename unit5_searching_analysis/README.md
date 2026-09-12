# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

Through this assignment, I developed a hands-on understanding of how Linear Search (O(n))
and Binary Search (O(log n)) operate under the hood. I gained practical experience
writing sequential iterations for linear search and applying divide-and-conquer
pointer logic (low, mid, high) for binary search. Comparing their performance across
small and large datasets reinforced how theoretical Big-O complexities translate
into real-world efficiency and how each algorithm handles boundary edge cases.

2. What challenges did you encounter, and how did you overcome them?

While implementing linear search was straightforward, binary search required much
more care when managing the search space. The main challenge was remembering to
correctly shift the low or high bounds past the midpoint (low = mid + 1 or high = mid - 1)
depending on whether the target was greater than or less than lst[mid]. I overcame
this by stepping through the logic manually to ensure the pointers continuously
narrowed the search space without causing infinite loops or skipping elements.

3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

Linear search is best suited for small, unsorted, or frequently changing datasets,
as well as one-off lookups where the O(n log n) cost of pre-sorting the data outweighs
the search time itself. Conversely, Binary Search is the clear choice for large,
pre-sorted datasets, such as database indexes, where millions of records need to
be queried instantly in O(log n) time. The primary tradeoff is setup and 
maintenance: Binary Search strictly requires sorted data, meaning frequent insertions
or deletions can introduce additional re-sorting overhead.